#메일 관련 라이브러리 임포트
import smtplib,ssl

from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.utils import formatdate
from email import encoders

class SendEmail:
    def __init__(self):
        pass
    
    def email_send_message(sender, receiver_list, msgRoot):
        #print(msgRoot, type(msgRoot))
        #print(msgRoot.as_string())
        smtp=smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp.login("email@","password")
        smtp.sendmail(sender, receiver_list, msgRoot.as_string() )
        smtp.quit()