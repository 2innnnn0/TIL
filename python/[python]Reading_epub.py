

# 1. BeautifulSoup 로 읽기.
# 음.. epub이 zip이 안풀어짐
# https://sssunho.tistory.com/59

import os
import zipfile
from bs4 import BeautifulSoup as BS



path_dir = '/Users/nathan/Library/Application Support/RIDI/Ridibooks/finsend/library/3414000006/'
file_name = '3414000006.epub'

path_dir+file_name
# for file in os.lisdir(path_dir)
with zipfile.ZipFile(path_dir+file_name,'r') as zf:
    zipInfo = zf.infolist()
    for member in zipInfo:
        if 'OEBPS' in member.filename:
            lxml = BS(zf.read(member.filename), 'lxml')
        # print(a)
            body_book = lxml.find_all('body', attrs={'class': 'book'})

            for p in body_book:
                print(p.text)
    # zf.close()

        # 출처: https://sssunho.tistory.com/59 [개발자 수노]
        # 3414000006.epub



zipfile.ZipFile('/Users/nathan/Library/Application Support/RIDI/Ridibooks/finsend/library/3414000006/3414000006.epub')




# 2. ebook 리딩패키지
# https://github.com/aerkalov/ebooklib
# !pip install ebooklib

import ebooklib
from ebooklib import epub

book = epub.read_epub(path_dir+file_name)

for image in book.get_items_of_type(ebooklib.ITEM_IMAGE):
    print(image)





# 3. 해킹. - 복호화까지해서 하드라.ㅋㅋ
# https://www.bpak.org/blog/2018/04/%EB%A6%AC%EB%94%94%EB%B6%81%EC%8A%A4-%EC%9E%90%EC%8B%A0%EC%9D%B4-%EC%86%8C%EC%9C%A0%ED%95%9C-%EC%B1%85-drm-%ED%95%B4%EC%A0%9C%ED%95%98%EA%B8%B0-feat-%EC%9C%84%ED%97%98%ED%95%9C-%EB%B9%84%EB%B0%80/
#
