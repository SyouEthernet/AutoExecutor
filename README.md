# AutoExecutor
the auto executor

通过此工具，实现定时执行对应的网络任务，且可以实现失败异常等情况监控

使用方法，在worker.py中写好自己需要执行的任务内容，在config.json配置好配置项，直接运行Drone.py


1.0版本相关内容：

a.能够实现定时执行任务 —— done

b.能够达成异常上报（通过推送/短信等途径完成，极光推送）—— done

c.能够在执行中查看异常发生等点，并记录 —— done

d.执行结果写入本地数据库，或serverless数据库，bmob云 —— done

e.使用json配置文件，不用停止drone即可以进行配置变更 —— done

f.所有的配置都放在一处，包括第三方依赖的key等，一次配置一键部署 —— done
