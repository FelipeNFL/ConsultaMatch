import unittest
import json
from modules.configFlask import ConfigFlask

class ConfigFlaskTest(unittest.TestCase):

    def test_init(self):
        file = open('config/flask.json','r')
        contentFile = file.read()
        file.close()
        contentFile = json.loads(contentFile)
        contentFile['port'] = 5000
        contentFile = json.dumps(contentFile)
        file = open('config/flask.json','w')
        file.write(contentFile)
        file.close()

        self.assertEqual(ConfigFlask().port,5000)
        

if __name__ == '__main__':
    unittest.main()
