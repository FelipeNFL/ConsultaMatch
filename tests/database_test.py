# coding: utf-8
import unittest
import json
from modules.database import Database
from modules.models.financier import Financier
from modules.models.company import Company

class DatabaseTest(unittest.TestCase):

    def test_getFinanciers(self):
        db = Database()
        db.insertFinancier(Financier(cnpj = "31.213.941/0001-37", name = "Financiador Teste 1", rate = 70, term = 72, warranty = "Terreno"))
        db.insertFinancier(Financier(cnpj = "24.642.112/0001-04", name = "Financiador Teste 2", rate = 70, term = 48, warranty = "Imóvel"))
        db.insertFinancier(Financier(cnpj = "19.576.165/0001-34", name = "Financiador Teste 3", rate = 35, term = 36, warranty = "Imóvel"))
        financiers = db.getFinanciers(rate = 70, term = 72, warranty = "Terreno")
        db.database.financier.delete_one({'cnpj' : "31.213.941/0001-37"})
        db.database.financier.delete_one({'cnpj' : "24.642.112/0001-04"})
        db.database.financier.delete_one({'cnpj' : "19.576.165/0001-34"})
        self.assertEquals(len(financiers),1)
        self.assertEquals(financiers[0].name, "Financiador Teste 1")
        self.assertEquals(financiers[0].rate, 70)
        self.assertEquals(financiers[0].term, 72)
        self.assertEquals(financiers[0].warranty, "Terreno")

    def test_insertFinancier(self):
        db = Database()
        db.insertFinancier(Financier(cnpj = "42.109.758/0001-02", name = "Financiador Teste 1", rate = 25, term = 72, warranty = "Terreno"))
        db.insertFinancier(Financier(cnpj = "42.742.578/0001-63", name = "Financiador Teste 2", rate = 25, term = 48, warranty = "Imóvel"))
        db.insertFinancier(Financier(cnpj = "45.441.634/0001-18", name = "Financiador Teste 3", rate = 35, term = 36, warranty = "Imóvel"))
        db.database.financier.delete_one({'cnpj' : "42.109.758/0001-02"})
        db.database.financier.delete_one({'cnpj' : "42.742.578/0001-63"})
        db.database.financier.delete_one({'cnpj' : "45.441.634/0001-18"})

    def test_getCompany(self):
        db = Database()
        db.insertCompany(Company(cnpj = "93.612.749/0001-70", name = "Companhia Teste 1", rate = 25, term = 72, warranty = "Terreno"))
        db.insertCompany(Company(cnpj = "27.456.797/0001-92", name = "Companhia Teste 2", rate = 25, term = 48, warranty = "Imóvel"))
        db.insertCompany(Company(cnpj = "26.805.322/0001-00", name = "Companhia Teste 3", rate = 35, term = 36, warranty = "Imóvel"))
        company = db.getCompany(cnpj = "93.612.749/0001-70")
        db.database.company.delete_one({'cnpj' : "93.612.749/0001-70"})
        db.database.company.delete_one({'cnpj' : "27.456.797/0001-92"})
        db.database.company.delete_one({'cnpj' : "26.805.322/0001-00"})
        self.assertEquals(company.name, "Companhia Teste 1")
        self.assertEquals(company.rate, 25)
        self.assertEquals(company.term, 72)
        self.assertEquals(company.warranty, "Terreno")

    def test_insertCompany(self):
        db = Database()
        db.insertCompany(Company(cnpj = "42.109.758/0001-02", name = "Companhia Teste 1", rate = 25, term = 72, warranty = "Terreno"))
        db.insertCompany(Company(cnpj = "42.742.578/0001-63", name = "Companhia Teste 2", rate = 25, term = 48, warranty = "Imóvel"))
        db.insertCompany(Company(cnpj = "45.441.634/0001-18", name = "Companhia Teste 3", rate = 35, term = 36, warranty = "Imóvel"))
        db.database.company.delete_one({'cnpj' : "42.109.758/0001-02"})
        db.database.company.delete_one({'cnpj' : "42.742.578/0001-63"})
        db.database.company.delete_one({'cnpj' : "45.441.634/0001-18"})

if __name__ == '__main__':
    unittest.main()
