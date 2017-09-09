# coding: utf-8
from modules.verifyCNPJ import CNPJ

class Financier():

    def __init__(self, name, cnpj, rate, term, warranty):
        if CNPJ(cnpj).valido() == True:
            self.cnpj = cnpj
        else:
            raise ValueError("O CNPJ informado não é válido")

        self.name = name
        self.rate = rate
        self.term = term
        self.warranty = warranty
