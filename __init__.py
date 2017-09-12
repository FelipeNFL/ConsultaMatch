# coding: utf-8
import json
from bson.json_util import dumps
from flask import Flask, request
from flask.json import jsonify
from flask.templating import render_template
from modules.database import Database
from modules.configFlask import ConfigFlask

app = Flask("ConsultaMatch")
db = Database()
config = ConfigFlask()

@app.route("/consult", methods = ['POST','GET'])
def getFinanciers():
    dataForm = request.form.to_dict()
    dataForm = json.loads(dumps(dataForm))

    try:
        company = db.getCompany(cnpj = dataForm['cnpj'])
    except ValueError as error:
        return renderIndex(error = str(error), cnpj = dataForm['cnpj'])
        
    try:
        financiers = db.getFinanciers(rate = company.rate, term = company.term, warranty = company.warranty)
    except ValueError:
        financiers = None

    return renderMatch(company = company, financiers = financiers)

@app.route("/")
def presentIndex():
    return renderIndex()

def renderIndex(error = "",cnpj = ""):
    return render_template('index.html', port = config.port, error = error, cnpj = cnpj)

def renderMatch(company = "", financiers = ""):
    return render_template('match.html', company = company, financiers = financiers, port = config.port)

app.run(port = config.port)
