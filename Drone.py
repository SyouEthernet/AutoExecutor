#基本执行框架
import ConfigLoader as confloader
import ErrorLogger as errorLogger
import executor.Worker as worker
import datetime
import time

# 本质就是一个死循环，在相隔一定的时间以后执行对应的事情
while 1:
    # 获取开始的时候都时间点
    startTimeStamp=datetime.datetime.now()

    # 通过configloader来加载配置
    # 以此来达到不结束进程的情况下修改配置，使下一次生效
    config = confloader.loadConfig()

    # 可以将要用到的配置项，付给变量，或者直接传到下面的dowork中当参数使用
    # 配置文件中拿到的等待时间
    waitTime = config['waitTime']
    
    # 开始执行相应工作任务，考虑到了可能有网络操作或者io的各种异常，因此需要用异常处理机制
    try:
        # 此处直接调用Worker.doWork()方法，
        # 业务变更实际需要开发重写的，仅有Worker.doWork()方法
        result = worker.doWork()
    except Exception as e:
        # 此处处理异常问题，可以考虑用文件记录
        errorLogger.log(e)
    finally:
        # 最后的通用执行，在此处理
        # 正常的result通常都是返回0的，不为0，表示有需要执行的步骤没有执行
        # 由于执行数据的写入数据库操作可以在dowork中进行，这里可以只处理异常的
        # 或者也可以在这里上报,通过极光推送进行推送 待完善
        print(result)

    # 这里是一次循环结束的时间点
    endTimeStamp = datetime.datetime.now()

    # 结束时间减去开始时间就是最后耗时，精确到秒
    costTime = (endTimeStamp-startTimeStamp).seconds

    # 本来要相隔一段时间进行一次任务的，但是可能存在任务耗时，所以减去
    # 当然，可以针对实际的策略动态规划
    waitTimeInFinal = waitTime - costTime

    # 等待这么久时间以后开始下一次循环
    time.sleep(waitTimeInFinal)
