import sqlite3  
from datetime import datetime
from time import sleep

#conditions idéales
niveauDEauIdeale = 0
humiditeIdeale = 0

conn = sqlite3.connect('AquaPonie') 
conn.execute("DROP TABLE donnees")
cur = conn.cursor() 

req = "CREATE TABLE donnees(date TEXT NOT NULL, niveauDEau BOOLEAN not null, humidite BOOLEAN not null)"  
cur.execute(req)
conn.commit() 

while True:
    now = datetime.now()
    date = now.strftime("%Y/%m/%d %H:%M:%S")

    #lire les données des capteurs

    niveauDEau = True       
    humidite = True

    cur.execute("Insert into donnees (`date` , `niveauDEau`, `humidite`) values (? , ? , ?)" , (date , niveauDEau , humidite) )
    conn.commit() 
    sleep(600) #10 minutes
 
conn.close 
