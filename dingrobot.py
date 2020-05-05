import requests

def push(url, contentString):    
    headers = {"Content-Type": "application/json;charset=utf-8"}
    content = {
        "msgtype": "text",
        "text": {
            "content": contentString
        },
        "at": {
    #        "atMobiles": [
    #            # 单独 @ 某个人
    #            "131xxxxxx81"
    #        ],
    #        "isAtAll": False
            # @ 所有人
           "isAtAll": True
        }
    }
    r = requests.post(url=url,headers=headers,json=content)