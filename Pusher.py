#推送器，此处使用极光推送，可以改成其他推送
import jpush

def push(app_key, master_secret, content):
    _jpush = jpush.JPush(app_key, master_secret)
    push = _jpush.create_push()
    push.audience = jpush.all_
    push.notification = jpush.notification(alert=content)
    push.platform = jpush.all_
    try:
        response=push.send()
    except common.Unauthorized:
        print ("Unauthorized")
    except common.APIConnectionException:
        print ("APIConnectionException")
    except common.JPushFailure:
        print ("JPushFailure")
    except:
        print ("Exception")