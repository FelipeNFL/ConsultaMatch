# coding: utf-8
import os
from modules.database import Database
from modules.models.financier import Financier
from modules.models.company import Company

os.system("pip install -r requirements.pip")
db = Database()

db.insertFinancier(Financier(cnpj = "42.109.758/0001-02", name = "Banco do Pernambuco", rate = 25, term = 72, warranty = "Terreno"))
db.insertFinancier(Financier(cnpj = "42.742.578/0001-63", name = "Banco Camargo de Araújo", rate = 10, term = 48, warranty = "Imóvel"))
db.insertFinancier(Financier(cnpj = "27.948.482/0001-62", name = "InovaCred", rate = 12, term = 36, warranty = "Terreno"))
db.insertFinancier(Financier(cnpj = "23.918.334/0001-44", name = "Banco do Pará", rate = 25, term = 72, warranty = "Terreno"))
db.insertFinancier(Financier(cnpj = "81.396.636/0001-04", name = "Dinheiro Certo", rate = 10, term = 48, warranty = "Imóvel"))
db.insertFinancier(Financier(cnpj = "38.265.772/0001-28", name = "CredFácil", rate = 12, term = 36, warranty = "Terreno"))

db.insertCompany(Company(cnpj = "18.259.473/0001-73", name = "Empreendimentos do Sol", rate = 25, term = 72, warranty = "Terreno"))
db.insertCompany(Company(cnpj = "14.886.257/0001-05", name = "Floricultura do Azevedo", rate = 25, term = 48, warranty = "Imóvel"))
db.insertCompany(Company(cnpj = "63.816.653/0001-63", name = "Bar's Rock", rate = 12, term = 36 , warranty = "Terreno"))
