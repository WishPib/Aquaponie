import sqlite3  

conn = sqlite3.connect('AquaPonie') 
cur = conn.cursor() 

req = "CREATE TABLE donnees(lumiere INTEGER not null, pH INTEGER not null, temperature INTEGER not null, niveauDEau INTEGER not null, humidite INTEGER not null)"  
cur.execute(req)  

#conditions idéales
lumiere = 0 
pH = 6.5 #[6, 7] 6 à 6.5?
temperature = 0
niveauDEau = 0
humidite = 0

cur.execute("Insert into donnees (`lumiere` , `pH` , `temperature` , `niveauDEau`, `humidite`) values (? , ? , ? , ?, ?)" , (lumiere , pH , temperature , niveauDEau , humidite) )
 
conn.commit()  
conn.close 