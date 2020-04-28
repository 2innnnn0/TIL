#스프레드 시트를 건드리기 위한 라이브러리
#스프레시트를 컨트롤 하려면, 스프레드시트에 (gspread-con@gspreadappproject-1350.iam.gserviceaccount.com)이 이메일 사용자를 공유해야함
import gspread
from oauth2client.service_account import ServiceAccountCredentials

import math
import pandas as pd
import numpy as np

import os
import sys

class SendSpreadsheet:
    def __init__(self):
        pass
    
    #spreadkey의 spreadsheet를 불러옴
    def set_spreadsheet(self, spreadsheet_key):
        #현재 파일 상대경로 받아오기 아이파이썬에서
        #path=os.getcwd()

        #현재 파일의 경로를 받아옵 크론잡에서 사용할 경우
        path = os.path.realpath(os.path.dirname(__file__))
        #print(os.path.realpath(os.path.dirname(__file__)))
        
        #스프레드 시트를 컨트롤 할 수 있는 google drive api에 연결하는 부분
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive','https://spreadsheets.google.com/feeds']

        SECRETS_FILE = path+'/.json'

        credentials = ServiceAccountCredentials.from_json_keyfile_name(SECRETS_FILE, SCOPES)

        gc = gspread.authorize(credentials)

        #출력하려는 spreadsheet의 키
        sh = gc.open_by_key(spreadsheet_key)
        
        return sh
    
    #읽어들인 spreadsheet 중 title에 해당하는 worksheet를 불러옴 
    def set_worksheet(self, sh, title):
        
        #워크시트에 설정한 타이틀과 동일한 스프레드 시트가 있는 지 체크하고 없으면 타이틀로 새로운 워크시트 생성
        sheet_list = sh.worksheets()
        new_spreadsheet = 1
        
        for sheet in sheet_list:
            if title == sheet.title:
                new_spreadsheet = 0
            else:
                pass
        
        #new_spreadsheet 가 1인 경우 시트를 만들고 컬럼을 추가한다
        if new_spreadsheet == 1:
            #이름에 맞춰 스프레드시트를 생성
            ws = sh.add_worksheet(title=title, rows=str(1), cols=str(col_length))
            
            #표에 컬럼을 생성<-한칸씩 업데이트
            j = 1
            for col in df.columns:
                ws.update_cell(1, j, col)
                j += 1
        
        #new_spreadsheet 가 1이 아닌 경우 기존에 시트가 시트를 불러오기만 함
        else :
            ws = sh.worksheet(title)
            
        return ws
    
    #스프레드 시트 주소, 스프레드 시트의 제목, 새로운 스프레드 시트인지 플래그(1: 신규, else: 있던 스프레드 시트), 몇번째 열부터 출력 할 것인가?(A열 : 1), 데이터 프레임
    def set_new_send_spreadsheet(self, ws, start_col, df):
        
        #데이터 프레임이 너무 커 한번에 스프레드 시트에 옮기지 못 할 경우 한번에 출력할 행수
        row_split = 200

        #한번에 출력할 행과 열 크기를 저장
        row_length = len(df.index)
        col_length = len(df.columns)
        x
        #내용이 많아 분할해서 자료를 넣어야 함(열이 길어 한번에 200행 씩 삽입)
        #spreadsheet에 반복해서 데이터 프레임을 분할 저장할 횟수를 설정
        max_index = math.ceil(row_length / row_split)
        
        #데이터 프레임의 내용을 worksheet 에 저장
        for i in range(max_index):

            #데이터 프레임을 스프레드 시트에 출력할 수 있도록 분할해서 sub 데이터 프레임을 만듦
            sub_df = df[(df.index >= (row_split * (i))) & (df.index < (row_split * (i + 1)))]

            #분할된 데이터 프레임의 행 수
            sub_row_length = len(sub_df.index)
            
            #현재 값이 있는 마지막 행 구하기(검사하는 열이 마지막 값까지 비어있는 행이 없어야됨.)
            #첫 열이 날짜인 경우가 높고, 무조건 적는 것으로 한다
            now_row_list = ws.col_values(start_col)
            last_row = len(now_row_list) - now_row_list.count('')

            #출력 해야하는 행 크기 만큼 현재 행이 되지 않을 경우 행 수를 늘려준다.
            if len(now_row_list) <= last_row + sub_row_length:
                #한번에 넣는 행 크기 만큼 행 늘리기
                ws.add_rows(int( sub_row_length ))
            else :
                pass

            #batch로 만들기 위해 시트에 들어갈 값을 저장하는 LIST를 만듦
            #시작하는 열이 달라지는 경우에 대응하기 위해 시작하는 start_cell_no와 end_cell_no를 받아 리스트를 불러온다.
            #List 형태: [<Cell R1C1 'value'>, <Cell R1C2 'value'>, <Cell R2C1 'value'>] 우에서 좌로 위에서 아래로
            start_cell_no = ws.get_addr_int(last_row + 1, start_col)
            end_cell_no = ws.get_addr_int((last_row + 1) + (sub_row_length - 1), start_col + (col_length-1))
            print(start_cell_no, end_cell_no, col_length)
            cell_list = ws.range(start_cell_no + ":" + end_cell_no)

            #결과 출력 (체크용)
            #print(str(i)+"번째 "+str(sub_row_length)+"줄 늘릴거야"+cell_no+"까지 늘려짐")

            #배치 단위로 넣기 위해 LIST에 값을 넣음 
            index = 0
            for cell in cell_list:
                row = int(index // col_length)
                col = int(index % col_length)
                cell.value = sub_df.iloc[row,col]
                index += 1

            #배치단위로 spreadsheet에 값 삽입
            ws.update_cells(cell_list)

            del sub_df
        del df
    
    #스프레드 시트 주소, 스프레드 시트의 제목, 새로운 스프레드 시트인지 플래그(1: 신규, else: 있던 스프레드 시트), 몇번째 열부터 출력 할 것인가?(A열 : 1), 데이터 프레임
    def set_send_spreadsheet(self, spreadsheet_key, title, start_col, df):
        
        #데이터 프레임이 너무 커 한번에 스프레드 시트에 옮기지 못 할 경우 한번에 출력할 행수
        row_split = 200

        #한번에 출력할 행과 열 크기를 저장
        row_length = len(df.index)
        col_length = len(df.columns)
        
        #내용이 많아 분할해서 자료를 넣어야 함(열이 길어 한번에 200행 씩 삽입)
        #spreadsheet에 반복해서 데이터 프레임을 분할 저장할 횟수를 설정
        max_index = math.ceil(row_length / row_split)
        
        #현재 파일 상대경로 받아오기 아이파이썬에서
        #path=os.getcwd()

        #현재 파일의 경로를 받아옵 크론잡에서 사용할 경우
        path = os.path.realpath(os.path.dirname(__file__))
        #print(os.path.realpath(os.path.dirname(__file__)))
        
        #스프레드 시트를 컨트롤 할 수 있는 google drive api에 연결하는 부분
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive','https://spreadsheets.google.com/feeds']

        SECRETS_FILE = path+'/.json'

        credentials = ServiceAccountCredentials.from_json_keyfile_name(SECRETS_FILE, SCOPES)

        gc = gspread.authorize(credentials)

        #출력하려는 spreadsheet의 키
        sh = gc.open_by_key(spreadsheet_key)
        
        #워크시트에 설정한 타이틀과 동일한 스프레드 시트가 있는 지 체크하고 없으면 타이틀로 새로운 워크시트 생성
        sheet_list = sh.worksheets()
        new_spreadsheet = 1
        
        for sheet in sheet_list:
            if title == sheet.title:
                new_spreadsheet = 0
            else:
                pass
        
        #new_spreadsheet 가 1인 경우 시트를 만들고 컬럼을 추가한다
        if new_spreadsheet == 1:
            #이름에 맞춰 스프레드시트를 생성
            ws = sh.add_worksheet(title=title, rows=str(1), cols=str(col_length))
            
            #표에 컬럼을 생성<-한칸씩 업데이트
            j = 1
            for col in df.columns:
                ws.update_cell(1, j, col)
                j += 1
        
        #new_spreadsheet 가 1이 아닌 경우 기존에 시트가 시트를 불러오기만 함
        else :
            ws = sh.worksheet(title)
        
        #데이터 프레임의 내용을 스프레드 시트에 저장
        for i in range(max_index):

            #데이터 프레임을 스프레드 시트에 출력할 수 있도록 분할해서 sub 데이터 프레임을 만듦
            sub_df = df[(df.index >= (row_split * (i))) & (df.index < (row_split * (i + 1)))]

            #분할된 데이터 프레임의 행 수
            sub_row_length = len(sub_df.index)
            
            #현재 값이 있는 마지막 행 구하기(검사하는 열이 마지막 값까지 비어있는 행이 없어야됨.)
            #첫 열이 날짜인 경우가 높고, 무조건 적는 것으로 한다
            now_row_list = ws.col_values(start_col)
            last_row = len(now_row_list) - now_row_list.count('')

            #출력 해야하는 행 크기 만큼 현재 행이 되지 않을 경우 행 수를 늘려준다.
            if len(now_row_list) <= last_row + sub_row_length:
                #한번에 넣는 행 크기 만큼 행 늘리기
                ws.add_rows(int( sub_row_length ))
            else :
                pass

            #batch로 만들기 위해 시트에 들어갈 값을 저장하는 LIST를 만듦
            #시작하는 열이 달라지는 경우에 대응하기 위해 시작하는 start_cell_no와 end_cell_no를 받아 리스트를 불러온다.
            #List 형태: [<Cell R1C1 'value'>, <Cell R1C2 'value'>, <Cell R2C1 'value'>] 우에서 좌로 위에서 아래로
            start_cell_no = ws.get_addr_int(last_row + 1, start_col)
            end_cell_no = ws.get_addr_int((last_row + 1) + (sub_row_length - 1), start_col + (col_length-1))
            print(start_cell_no, end_cell_no, col_length)
            cell_list = ws.range(start_cell_no + ":" + end_cell_no)

            #결과 출력 (체크용)
            #print(str(i)+"번째 "+str(sub_row_length)+"줄 늘릴거야"+cell_no+"까지 늘려짐")

            #배치 단위로 넣기 위해 LIST에 값을 넣음 
            index = 0
            for cell in cell_list:
                row = int(index // col_length)
                col = int(index % col_length)
                cell.value = sub_df.iloc[row,col]
                index += 1

            #배치단위로 spreadsheet에 값 삽입
            ws.update_cells(cell_list)

            del sub_df
        del df