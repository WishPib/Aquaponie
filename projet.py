import sqlite3  
from datetime import datetime
import time

#conditions idéales
lumiereIdeale = 0 
pHIdeale = 6.5 #[6, 7] 6 à 6.5?
temperatureIdeale = 0
niveauDEauIdeale = 0
humiditeIdeale = 0

conn = sqlite3.connect('AquaPonie') 
conn.execute("DROP TABLE donnees")
cur = conn.cursor() 

req = "CREATE TABLE donnees(date TEXT NOT NULL, lumiere INTEGER not null, pH INTEGER not null, temperature INTEGER not null, niveauDEau INTEGER not null, humidite INTEGER not null)"  
cur.execute(req)
conn.commit() 

while True(): #Il faut trouver une bonne manière de garder cette boucle pour qu'elle n'arrête pas de run
    now = datetime.now()
    date = now.strftime("%Y/%m/%d %H:%M:%S")

    #lire les données des capteurs
    lumiere = 1 
    pH = 2
    temperature = 3
    niveauDEau = 4
    humidite = 5

    cur.execute("Insert into donnees (`date` , `lumiere` , `pH` , `temperature` , `niveauDEau`, `humidite`) values (? , ? , ? , ? , ?, ?)" , (date , lumiere , pH , temperature , niveauDEau , humidite) )
    conn.commit() 
    time.sleep(600) #à chaque 10 minutes(10*60), refaire la boucle
 
conn.close 
