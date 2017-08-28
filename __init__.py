# coding: utf-8
import json

from bson.json_util import dumps
from flask import Flask, request
from flask.json import jsonify
from flask.templating import render_template

from modules.Database import Database
from modules.Person import Person


app = Flask("ConsultaNomeHTTP")
db = Database()

@app.route("/consulta", methods = ['POST'])
def getCPF():
    dadosForm = request.form.to_dict()
    dadosForm = json.loads(dumps(dadosForm))
    
    try:
        person = db.getPersonByCPF(dadosForm['cpf'])
    except ValueError as error:
        return render_template('index.html', nome = error, cpf = dadosForm["cpf"])
    
    return render_template('index.html', nome = person.name, cpf = person.cpf)

@app.route("/")
def apresentarIndex():
    return render_template('index.html')

app.run()