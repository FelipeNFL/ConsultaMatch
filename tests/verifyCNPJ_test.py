import unittest
from modules.verifyCNPJ import CNPJ

class CNPJTest(unittest.TestCase):

    def test_init(self):

        #Adaptação dos testes já pre-determinados na classe, só que usado o unittest e "não assert"

        a = CNPJ('11222333000181')
        b = CNPJ('11.222.333/0001-81')
        c = CNPJ([1, 1, 2, 2, 2, 3, 3, 3, 0, 0, 0, 1, 8, 2])

        self.assertTrue(a.valido())
        self.assertTrue(b.valido())
        self.assertFalse(c.valido())
        self.assertEquals(a,b)
        self.assertNotEquals(b,c)
        self.assertNotEquals(a,c)
        self.assertEquals(eval(repr(a)),a)
        self.assertEquals(eval(repr(b)),b)
        self.assertEquals(eval(repr(c)),c)
        self.assertEquals(str(a),"11.222.333/0001-81")
        self.assertEquals(str(b),str(a))
        self.assertEquals(str(c),"11.222.333/0001-82")

if __name__ == '__main__':
    unittest.main()
