# coding: utf-8
import json
from bson.json_util import dumps
from flask import Flask, request
from flask.json import jsonify
from flask.templating import render_template
from modules.database import Database

app = Flask("ConsultaMatch")
db = Database()

@app.route("/consult", methods = ['POST','GET'])
def getFinanciers():
    dataForm = request.form.to_dict()
    dataForm = json.loads(dumps(dataForm))

    try:
        company = db.getCompany(cnpj = dataForm['cnpj'])
    except ValueError as error:
        return render_template('index.html', error = str(error).decode(encoding='UTF-8'), cnpj = dataForm['cnpj'])

    try:
        financiers = db.getFinanciers(rate = company.rate, term = company.term, warranty = company.warranty)
    except ValueError:
        financiers = None

    return render_template('match.html', company = company, financiers = financiers)

@app.route("/")
def apresentarIndex():
    return render_template('index.html')

app.run()
