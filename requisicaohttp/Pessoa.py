from BancoDeDados import BancoDeDados
import json
from bson.json_util import dumps

class Pessoa(object):

    @staticmethod
    def consultarNome(cpf):
        db = BancoDeDados() #Cria uma instância do banco de dados
        consulta = BancoDeDados().consultar({'cpf': cpf}) #Realiza uma consulta passando o cpf como filtro
        #dumps() serializa os resultados da consulta para o formato JSON
        #loads() carrega o JSON serializado
        consulta = json.loads(dumps(consulta))
<<<<<<< HEAD
        if consulta != None:
            return consulta["nome"] #Depois que o JSON é serializado é possível filtrar o valor pela chave
        else:
            return consulta #Se for none, retorne esse valor
=======
        return consulta["nome"] #Depois que o JSON é serializado é possível filtrar o valor pela chave
>>>>>>> 720184f33a04e6ffdcca8d7f129840ce7b2c1866
        pass
