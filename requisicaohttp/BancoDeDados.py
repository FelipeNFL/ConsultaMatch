from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from pymongo.cursor import Cursor

class BancoDeDados(object):
    def __init__(self):
        #Cria uma instância do MongoDB:
        self.client = MongoClient()
        #Seleciona a coleção que contém os cpfs no banco de dados:
        self.collection = Collection(self.client.get_database("pessoas"), "pessoas")

    def consultar(self, filtro):
        #Retorna os registros contidos na collection de acordo com o parâmetro filtro:
        return MongoClient().get_database("pessoas").get_collection("pessoas").find_one(filtro)