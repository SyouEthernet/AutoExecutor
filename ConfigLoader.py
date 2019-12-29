#配置加载器
import json

def loadConfig(path='./config.json'):
    configFile = open(path, 'r')
    configString = configFile.read()
    configJson = json.loads(configString)
    configFile.close()
    return configJson