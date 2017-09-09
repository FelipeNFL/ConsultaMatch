import unittest
from modules.models.financier import Financier

class financierTest(unittest.TestCase):

    def test_set_atributtes(self):
        financier = Financier(cnpj = "42.109.758/0001-02", name = "Financiador Teste", rate = 25, term = 72, warranty = "Terreno")

        self.assertEquals(financier.cnpj, "42.109.758/0001-02")
        self.assertEquals(financier.name, "Financiador Teste")
        self.assertEquals(financier.rate, 25)
        self.assertEquals(financier.term, 72)
        self.assertEquals(financier.warranty, "Terreno")

    def test_cnpj_error(self):
        with self.assertRaises(ValueError):
            Financier(cnpj = "11.111.111/1111-11", name = "Financiador Teste", rate = 25, term = 72, warranty = "Terreno")

if __name__ == '__main__':
    unittest.main()
