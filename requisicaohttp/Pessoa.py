from BancoDeDados import BancoDeDados
import json
from bson.json_util import dumps

class Pessoa(object):

    @staticmethod
    def consultarNome(cpf):
        db = BancoDeDados() #Cria uma inst�ncia do banco de dados
        consulta = BancoDeDados().consultar({'cpf': cpf}) #Realiza uma consulta passando o cpf como filtro
        #dumps() serializa os resultados da consulta para o formato JSON
        #loads() carrega o JSON serializado
        consulta = json.loads(dumps(consulta))
        return consulta["nome"] #Depois que o JSON � serializado, � poss�vel filtrar o valor pela chave
        pass
