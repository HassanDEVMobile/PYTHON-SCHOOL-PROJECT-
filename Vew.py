from typing import List
import sqlite3

from Model import Match


class Vew:
    id = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
       return self.name,self.age
vew = Vew("Hassan",18)


xt = Vew("Adoul",23)

class DB :
    def add(self,vew:Vew) :
        conn = sqlite3.connect('Vew.db')
        c = conn.cursor()
        c.execute("""
        INSERT INTO Vew (nome,age)
        VALUES (?,?)""",(vew))
        conn.commit()
        conn.close()
montuple = tuple(xt.__dict__.values())
db = DB()

db.add(montuple)
conn = sqlite3.connect('Vew.db')
c = conn.cursor()
c.execute("SELECT * FROM Vew WHERE id = 5")
result = c.fetchone()
print(result[1])

class Verrouille :
     def __init__(self,name,age):
         self.name = name
         self.age = age
     def __init_(self,name):
         self.name = name
