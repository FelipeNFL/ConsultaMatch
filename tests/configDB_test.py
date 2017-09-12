import unittest
import json
from modules.configDB import ConfigDB

class ConfigDBTest(unittest.TestCase):

    def test_init(self):
        file = open('config/database.json','r')
        contentFile = file.read()
        file.close()
        contentFile = json.loads(contentFile)
        contentFile['port'] = 27017
        contentFile = json.dumps(contentFile)
        file = open('config/database.json','w')
        file.write(contentFile)
        file.close()

        self.assertEqual(ConfigDB().port,27017)
        

if __name__ == '__main__':
    unittest.main()
