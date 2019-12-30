from executor.bmob import *

def doWork(step=0, **args):
    executeStep = step
    print('hello, drone!')
    # 初始化一个bmob，如果不使用bmob可以考虑使用别的替代
    b = Bmob(args['bmobApi'], args['bmobKey'])
    b.insert(
        'test', # 表名
        { # 额外信息
            "content": "测试数据",
            "user": BmobPointer("_User", "xxx"), # Pointer类型
            "date": BmobDate(1545098009351) ## Date类型
        }
    ).jsonData # 输出json格式的内容
    return executeStep