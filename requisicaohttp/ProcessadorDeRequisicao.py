# coding: utf-8
from Pessoa import Pessoa
from flask import Flask, request
from flask.json import jsonify
from bson.json_util import dumps
import json
from flask.templating import render_template

app = Flask("RequisicaoHTTP")

@app.route("/consulta", methods = ['POST'])
def realizarConsultaDeCPF():
    dadosForm = request.form.to_dict() #Recebe os dados enviados por um form
    
    #dumps() serializa os dados do formulário para o formato JSON
    #loads() carrega o JSON serializado
    dadosForm = json.loads(dumps(dadosForm))
    nome = Pessoa.consultarNome(dadosForm["cpf"])
    
    if nome != None:
        return render_template('index.html', nome = Pessoa.consultarNome(dadosForm["cpf"]), cpf = dadosForm["cpf"])
    else:
        return render_template('index.html', nome = "Erro! Confira se o CPF digitado está correto", cpf = dadosForm["cpf"])
        

@app.route("/")
def apresentarIndex():
    #Caso não seja passado nenhum parâmetro, a index será exibida com o formulário vazio
    return render_template('index.html', nome = "", cpf="")

app.run()
