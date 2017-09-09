import unittest
from modules.models.company import Company

class CompanyTest(unittest.TestCase):

    def test_set_atributtes(self):
        company = Company(cnpj = "42.109.758/0001-02", name = "Companhia Teste", rate = 25, term = 72, warranty = "Terreno")

        self.assertEquals(company.cnpj, "42.109.758/0001-02")
        self.assertEquals(company.name, "Companhia Teste")
        self.assertEquals(company.rate, 25)
        self.assertEquals(company.term, 72)
        self.assertEquals(company.warranty, "Terreno")

    def test_cnpj_error(self):
        with self.assertRaises(ValueError):
            Company(cnpj = "11.111.111/1111-11", name = "Companhia Teste", rate = 25, term = 72, warranty = "Terreno")

if __name__ == '__main__':
    unittest.main()
