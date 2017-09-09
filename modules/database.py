# coding: utf-8
import json

from pymongo import MongoClient
from modules.models.financier import Financier
from modules.models.company import Company

class Database():

    def __init__(self):
        fileConfig = open('config/database.json','r')
        configs = json.loads(fileConfig.read())

        self.client = MongoClient()

        if(str(configs['port']) != ''):
            self.client = MongoClient(port = int(configs['port']))

        self.database = self.client.credit
        fileConfig.close()

    def insertFinancier(self, financier):
        if self.database.financier.insert_one({'cnpj' : financier.cnpj, 'name' : financier.name, 'rate' : financier.rate, 'term' : financier.term, 'warranty' : financier.warranty}).acknowledged == False:
            raise Exception("Ocorreu um erro ao inserir o documento na coleção de financiadores no banco de dados")

    def getFinanciers(self, rate = "", term = "", warranty = ""):
        filters = {}
        if rate != "":
            filters['rate'] = rate
        if term != "":
            filters['term'] = term
        if warranty != "":
            filters['warranty'] = warranty

        cursor = self.database.financier.find(filters)
        financiers = []
        if cursor.count() != 0:
            for result in cursor:
                financiers.insert(len(financiers),Financier(cnpj = result['cnpj'], name = result['name'], rate = result['rate'], term = result['term'], warranty = result['warranty']))
            return financiers
        else:
            raise ValueError("Não foram encontrados financiadores compatíveis com o perfil descrito")

    def insertCompany(self, company):
        if self.database.company.insert_one({'cnpj' : company.cnpj, 'name' : company.name, 'rate' : company.rate, 'term' : company.term, 'warranty' : company.warranty}) == False:
            raise Exception("Ocorreu um erro ao inserir o documento na coleção de empresas no banco de dados")

    def getCompany(self, cnpj = ""):
        result = self.database.company.find_one({'cnpj' : cnpj})
        if result != None:
            return Company(cnpj = result['cnpj'], name = result['name'], rate = result['rate'], term = result['term'], warranty = result['warranty'])
        else:
            raise ValueError("Não há empresa cadastrada sob esse CNPJ no sistema")
