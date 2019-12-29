# 错误处理器
def log(error, path='error.log'):
    errorLog = open(path, 'a')
    # 先空一行
    errorLog.write('\n')
    # 写入错误记录
    errorLog.write(error)
    errorLog.close()