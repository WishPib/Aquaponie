# Aquaponie <a name="Aquaponie"></a>  <!--https://stackoverflow.com/questions/11948245/markdown-to-create-pages-and-table-of-contents-->
L’aquaponie est un système fermé où des plantes ou bien des légumes sont alimentées avec de l’eau qui contient des nutriments. Cette eau avec les nutriments viendrait d’un autre bassin d’eau qui contiendrait des poissons qui relâcheront ces nutriments après avoir mangé de la nourriture. Le bassin avec les poissons est rempli par l’eau qui passe à travers les plantes ou les légumes, comme vu ci-dessous. 

![schema-composants-aquaponie](https://github.com/WishPib/Aquaponie/assets/157630823/ae3ba559-eeb1-488e-b1b1-b1f69d71db17)

Le but de ce projet, c’est de prendre ce système à une dimension plus complexe en essayant de l'automatiser et d’évaluer sa situation en observant ses données qui la définissent sur un site web. Avec le matériel nécessaire, une partie du travail nécessaire pour prendre soin de votre potager sera facilité, puisque qu'il sera fait automatiquement.

## Table des matières
- [Introduction](#Aquaponie)
- [Projet](#Projet)
  - [Matériel nécessaire](#Matériel)
  - [Installations à faire](#Installations)
  - [Schémas](#Schémas)
  - [Guide d'utilisation](#utilisation)
- [Conclusion](#Conclusion)
  - [Autheurs](#Autheurs)

## Projet <a name="Projet"></a>
Voici les détails nécessaire pour que vous repreniez personnellement ce projet, incluant le matériel physique, les installations à faire sur vos appareils électronique si vous ne les aviez pas encore, comment tout assembler ça et comment l'utiliser. Pour cette section, gardez en tête que c'est ce que nous avons utilisé pour réaliser notre projet. Si vous voulez faire un changement qui sera plus approprié à vos besoins, vous avez une pièce qui ne fonctionne pas ou bien vous n'avez pas et ne pouvez pas avoir une certaine partie du système, n'oubliez pas que le remplacement que vous utilisiez ne marcherait peut-être pas avec notre code.
### Matériel nécessaire <a name="Matériel"></a>
La pièce centrale du système est le Raspberry Pi 4 modèle B. C'est un ordinateur réduit qu’on utilisera pour connecter les capteurs ensembles et pour traiter les données obtenues. On l’a choisi parce qu’il est très bon dans des projets automatiques personnels, grâce à ses broches GPIO (General-Purpose Input/Output). 
![616RFn6Jv5L _AC_SL1024_](https://github.com/WishPib/Aquaponie/assets/157630823/340560d8-9779-4581-a3cc-9e6a26ad6836)

Vous aurez besoin d'un Ti-Cobbler Plus, une extension pour le Raspberry pi qui permet de connecter toutes ses brochures GPIO à une planche à pain électronique. Bien sûr, vous aurez besoin de fils GPIO pour tout connecter ensemble.
![71tOdqMmm9L _SL1200_](https://github.com/WishPib/Aquaponie/assets/157630823/b3812c87-ef3a-4d61-bf9c-582f0636cdd8)

Maintenant, parlons de nos capteurs. Placé dans le bassin de poissons et connecté à un convertisseur de signal analogue-digital ADS1115, le capteur de niveau d'eau IDUINO SE045 détecte si le niveau d’eau est trop bas et qu’il faut ajouter de l’eau dans le système, ou si le niveau d’eau est trop haut et qu’il faut activer la pompe pour faire circuler l’eau vers les plantations. Puis, inséré dans la terre humide des plantes, un capteur d'humidité composé d’une électrode en fourchette et d’un module de conversion détermine, après calibration du potentiomètre, le niveau d’humidité de la terre idéal. Capteur provenant de AZDelivery avec un convertisseur analogue-digital Digital flying fish. 

Finalement, il y a la pome d'eau, le modèle DC DIY qui vient de INTLAB et qui a un moteur 12V et 5W permettant la circulation de l’eau du bassin de poissons vers les plantes.
### Installations à faire <a name="Installations"></a>
### Schémas <a name="Schémas"></a>
### Guide d'utilisation <a name="utilisation"></a>

## Conclusion <a name="Conclusion"></a>
Pour résumer, ce projet est notre manière d'automatiser un système d'aquaponie. Si vous avez le matériel nécessaire
### Autheurs <a name="Autheurs"></a>
Raphaël Hoffmann, Raphaël Charabaty, Shunyi Wang et Victor Alexandre Frings-Morales sont tous des étudiants dans le programme de Sciences, informatique et mathématique au Collège Bois de Boulogne à Montréal. Ils ont fait ce projet d’aquaponie pour leur dernier cours de programmation dans leur programme, le cours de projet d’intégration en sciences informatiques et mathématiques.
