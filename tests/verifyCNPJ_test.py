import unittest
from modules.verifyCNPJ import CNPJ

class CNPJTest(unittest.TestCase):

    def test_init(self):

        #Adaptação dos testes já pre-determinados na classe ao unittest

        a = CNPJ('11222333000181')
        b = CNPJ('11.222.333/0001-81')
        c = CNPJ([1, 1, 2, 2, 2, 3, 3, 3, 0, 0, 0, 1, 8, 2])

        self.assertTrue(a.valido())
        self.assertTrue(b.valido())
        self.assertFalse(c.valido())
        self.assertEqual(a,b)
        self.assertNotEqual(b,c)
        self.assertNotEqual(a,c)
        self.assertEqual(eval(repr(a)),a)
        self.assertEqual(eval(repr(b)),b)
        self.assertEqual(eval(repr(c)),c)
        self.assertEqual(str(a),"11.222.333/0001-81")
        self.assertEqual(str(b),str(a))
        self.assertEqual(str(c),"11.222.333/0001-82")

if __name__ == '__main__':
    unittest.main()
