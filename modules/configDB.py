# coding: utf-8

import json

class ConfigDB():
    def __init__(self):
        fileConfig = open('config/database.json','r')
        configs = json.loads(fileConfig.read())
        self.port = configs['port']
        fileConfig.close()
