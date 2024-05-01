import sqlite3  
from datetime import datetime
from time import sleep
import os



conn = sqlite3.connect('/home/aquaponie/Aquaponie/aquaponieDB.db') #nom du DB
cur = conn.cursor()

def resetBD():
    conn.execute("DROP TABLE mesures")
    req = "CREATE TABLE mesures(date TEXT, niveauDEau BOOLEAN, humidite BOOLEAN)"  
    cur.execute(req)
    conn.commit() 
 

def envoyerBD(niveauDEau,humidite):
    now = datetime.now()
    date = now.strftime("%Y/%m/%d %H:%M:%S")

    #lire les données des capteurs

    cur.execute("Insert into mesures (`date` , `niveauDEau`, `humidite`) values (? , ? , ?)" , (date , niveauDEau , humidite) )
    conn.commit() 
 
conn.close 
