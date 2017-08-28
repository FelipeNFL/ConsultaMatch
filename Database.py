# coding: utf-8
from pymongo import MongoClient
from VerifyCPF import CPF
import json
from Person import Person

class Database():

    def __init__(self):
        fileConfig = open('config/database.json')
        configs = json.loads(fileConfig.read())
        
        if configs['username'] != "" and configs["password"] != "":
            self.client = MongoClient(port = configs['port'], username = configs['username'], password = configs['password'])
        elif configs['port'] != "":
            self.client = MongoClient(port=configs['port'])
        else:
            self.client = MongoClient()
        
        self.database = self.client.get_database("pessoas")
        
    def getPersonByCPF(self,cpf):
        if(CPF(cpf).isValid()):
            result = self.database.get_collection('pessoas').find_one({'cpf': cpf})
            if result != None:
                return Person(result['cpf'],result['name'])
            else:
                raise ValueError('O CPF específicado não consta na base de dados')
        else:
            raise ValueError("Esse CPF não existe")