# coding: utf-8

import json

class ConfigFlask():
    def __init__(self):
        fileConfig = open('config/flask.json','r')
        configs = json.loads(fileConfig.read())
        self.port = configs['port']
        fileConfig.close()
