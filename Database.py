# coding: utf-8
from pymongo import MongoClient
from VerifyCPF import CPF
import json
from Person import Person

class Database():

    def __init__(self):
        fileConfig = open('config/database.json')
        configs = json.load(fileConfig.readlines())
        fileConfig.close()

        self.client = MongoClient(port = configs['port'], username = configs['username'], password = configs['password'])
        self.database = self.client.getdatabase('pessoas')
        
    def getPersonByCPF(self,cpf):
        if(CPF(cpf).isValid()):
            registro = self.database.get_collection('pessoas').find_one({'cpf': cpf})
            return Person(registro['cpf'],registro['name'])
        else:
            raise ValueError("Esse CPF não existe")