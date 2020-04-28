import slackweb

#slack 토큰: https://hooks.slack.com/services/xxxxx

class SendSlack:
    def __init__(self):
        pass
    
    #slack 이외의 내용은 **args 형태로 변수가 가변적인 경우 받을 때 사용하는 것
    #attachement를 **args로 받을 거
    #title과 sender는 꼭 필요하지만, attachment는 상황에 따라 필요하지 않을 수도 있기 때문에 가변 변수에 넣음
    def set_send_slack(token, title, sender, **kwargs):
        
        print(len(kwargs))
        
        #토큰을 통해 해당 채널에 접속
        slack = slackweb.Slack(url = token)
        
        if len(kwargs) >= 1:
            attachments = kwargs['attachements']
            
            #내역 slack 으로 전송
            #text : 슬랙 메세지 제목, username :  보내는 사람, attachments :  보내는 내역
            slack.notify(text = title, username = sender, attachments = attachments)
            
        else:
            #내역 slack 으로 전송
            #text : 슬랙 메세지 제목, username :  보내는 사람,
            slack.notify(text = title, username = sender)