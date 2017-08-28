# coding: utf-8
import json

from Person import Person
from bson.json_util import dumps
from flask import Flask, request
from flask.json import jsonify
from flask.templating import render_template
from Database import Database

db = Database()

app = Flask("RequisicaoHTTP")

@app.route("/consulta", methods = ['POST'])
def getCPF():
    dadosForm = request.form.to_dict()
    dadosForm = json.loads(dumps(dadosForm))
    
    try:
        person = db.getPersonByCPF(dadosForm['cpf'])
    except ValueError:
        return render_template('index.html', nome = "Erro! O CPF informado não existe", cpf = dadosForm["cpf"])
    
    return render_template('index.html', nome = person.name, cpf = person.cpf)
        

@app.route("/")
def apresentarIndex():
    #Caso não seja passado nenhum parâmetro, a index será exibida com o formulário vazio
    return render_template('index.html')

app.run()
