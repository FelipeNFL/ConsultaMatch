# coding: utf-8
import os
from modules.Database import Database
from modules.Person import Person

os.system("pip install -r requirements.pip")
db = Database()
db.insertPerson(Person("072.597.741-85","Felipe Nunes de Freitas Lima"))
db.insertPerson(Person("412.140.554-43","João Ferreira Martins"))
db.insertPerson(Person("812.618.438-86","Carla Aleluia da Silva"))
