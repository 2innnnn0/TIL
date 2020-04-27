# Load Package
import pandas as pd
import numpy as np
import datetime as dt
import os
import sys

# mail
import smtplib
import ssl

from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.utils import formatdate
from email import encoders


query = '''
select *
from LIST
'''

# 메일 라이브러리
# class SendEmail:
# 1. 클래스 시작
def __init__(self):
pass
# 2. 이메일 계정 접속
def email_send_message(sender, receiver_list, msgRoot):
#print(msgRoot, type(msgRoot))
#print(msgRoot.as_string())
smtp=smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtp.login("email@","password")
smtp.sendmail(sender, receiver_list, msgRoot.as_string() )
smtp.quit()

# 3. 본문작성
#차량 세차 현황 메일에 텍스트 부분을 작성하기 위한 데이터 프레임을 생성하고 그것을 메일에 넣음
def set_mail_text( df, now_at) :
mail_text = '안녕하세요 <br> 입니다.<br>'
mail_text += '<br>잘전송되라! 끗<br>'
return mail_text

# 4. 메일발송
def set_mail_form(mail_text, *args):
print(args)
# 송신자 , 수신자 설정
sender = 'email@'
receiver_list = ['email@'] 
print(sender, receiver_list)

# 메일보내기
# 메일의 기초 내용을 만드는 부분
msgRoot = MIMEMultipart('related')

# 제목
msgRoot['Subject'] = '[abc]' + args[2].strftime('%Y년%m월%d일') + '_리스트'
msgRoot['From'] = sender
msgRoot['To'] = 'email@'

# alternative 안에 본문 내용을 캡슐화해서 첨부한 이미지의 ID를 불러와 화면에 표시하게 해줄 수 있다.
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('메일입니다')
msgAlternative.attach(msgText)

# 메일에 본문을 'alternative' 부분에 내용첨부
msgText = MIMEText(mail_text, 'html')
msgAlternative.attach(msgText)

# 끗
send_email.SendEmail.email_send_message(sender, receiver_list, msgRoot)
