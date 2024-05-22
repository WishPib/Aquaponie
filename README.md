# Aquaponie <a name="Aquaponie"></a>  <!--https://stackoverflow.com/questions/11948245/markdown-to-create-pages-and-table-of-contents-->
L’aquaponie est un système fermé où des plantes ou bien des légumes sont alimentées avec de l’eau qui contient des nutriments. Cette eau avec les nutriments viendrait d’un autre bassin d’eau qui contiendrait des poissons qui relâcheront ces nutriments après avoir mangé de la nourriture. Le bassin avec les poissons est rempli par l’eau qui passe à travers les plantes ou les légumes, comme vu ci-dessous. 

![schema-composants-aquaponie](https://github.com/WishPib/Aquaponie/assets/157630823/ae3ba559-eeb1-488e-b1b1-b1f69d71db17)

Le but de ce projet, c’est de prendre ce système à une dimension plus complexe en essayant de l'automatiser et d’évaluer sa situation en observant ses données qui la définissent sur un site web. Avec le matériel nécessaire, une partie du travail nécessaire pour prendre soin de votre potager sera facilité, puisque qu'il sera fait automatiquement.

## Table des matières
- [Introduction](#Aquaponie)
- [Méthode](#Méthode)
  - [Matériel nécessaire](#Matériel)
  - [Installations à faire](#Installations)
  - [Schémas](#Schémas)
    - [Diagramme de pièces](#pièces)
    - [Diagramme de classes](#classes)
    - [Diagramme de cas d'utilisation](#utilisation)
  - [Guide d'utilisation](#Guide)
- [Résultas](#Résultas)
- [Discussion](#Discussion)
- [Conclusion](#Conclusion)
  - [Autheurs](#Autheurs)

## Méthode <a name="Méthode"></a>
Voici les détails nécessaire pour que vous repreniez personnellement ce projet, incluant le matériel physique, les installations à faire sur vos appareils électronique si vous ne les aviez pas encore, comment tout assembler ça et comment l'utiliser. Pour cette section, gardez en tête que c'est ce que nous avons utilisé pour réaliser notre projet. Si vous voulez faire un changement qui sera plus approprié à vos besoins, vous avez une pièce qui ne fonctionne pas ou bien vous n'avez pas et ne pouvez pas avoir une certaine partie du système, n'oubliez pas que le remplacement que vous utilisiez ne marcherait peut-être pas avec notre code. On assume aussi que vous vous êtes déjà procuré d'un potager ou un jardin, des poissons et le matériel nécessaire à maintenir ces deux éléments comme de la nourriture et un grand bac, car cette partie est plus subjective. Voici une idée à ce quoi ce système ressemblera:

https://www.aquaponie.fr/les-elements-dun-systeme-aquaponique/
### Matériel nécessaire <a name="Matériel"></a>
La pièce centrale du système est le Raspberry Pi 4 modèle B. C'est un ordinateur réduit qu’on utilisera pour connecter les capteurs ensembles et pour traiter les données obtenues. On l’a choisi parce qu’il est très bon dans des projets automatiques personnels, grâce à ses broches GPIO (General-Purpose Input/Output). Une carte SD d'au moins 16GB est aussi nécessaire.

![616RFn6Jv5L _AC_SL1024_](https://github.com/WishPib/Aquaponie/assets/157630823/340560d8-9779-4581-a3cc-9e6a26ad6836)

Vous aurez besoin d'un Ti-Cobbler Plus, une extension pour le Raspberry pi qui permet de connecter toutes ses brochures GPIO à une planche à pain électronique. Bien sûr, vous aurez besoin de fils GPIO pour tout connecter ensemble.

![71tOdqMmm9L _SL1200_](https://github.com/WishPib/Aquaponie/assets/157630823/b3812c87-ef3a-4d61-bf9c-582f0636cdd8)

Maintenant, parlons de nos capteurs. Placé dans le bassin de poissons et connecté à un convertisseur de signal analogue-digital ADS1115, le capteur de niveau d'eau IDUINO SE045 détecte si le niveau d’eau est trop bas et qu’il faut ajouter de l’eau dans le système, ou si le niveau d’eau est trop haut et qu’il faut activer la pompe pour faire circuler l’eau vers les plantations. Puis, inséré dans la terre humide des plantes, un capteur d'humidité composé d’une électrode en fourchette et d’un module de conversion détermine, après calibration du potentiomètre, le niveau d’humidité de la terre idéal. Capteur provenant de AZDelivery avec un convertisseur analogue-digital Digital flying fish. 

![download](https://github.com/WishPib/Aquaponie/assets/157630823/a2a8c645-34e4-4d8a-840d-422dec71bd6b)
![download](https://github.com/WishPib/Aquaponie/assets/157630823/558db036-2a74-4a2f-8243-aaa05fdfc245)

Finalement, il y a la pompe d'eau, le modèle DC DIY qui vient de INTLAB et qui a un moteur 12V et 5W permettant la circulation de l’eau du bassin de poissons vers les plantes. Vous aurez besoin d'extensions pour avoir plus de liberté du placement de la pompe.

![Intllab-17ml-min](https://github.com/WishPib/Aquaponie/assets/157630823/8f8ac74e-fda7-4e26-9d83-a51e04d92ad8)

Il est aussi idéal d'avoir un ordinateur pour faciliter l'installation des systèmes et applications. Ceci est le minimum nécessaire à ce projet. Vous pouvez acheter ces pièces où vous voulez, le meilleur endroit n'est pas le même partout. Si vous voulez ajouter plus de choses, il y aura probablement du code à ajouter et des installations à faire. Voyons donc maintenant les intallations de base à faire.
### Installations à faire <a name="Installations"></a>
Il faut commencer par préparer le Raspberry pi. C'est ici qu'on utilisera la carte SD pour installer le système d'exploitation dans l'appareil. Vous pouvez suivre les instructions sur le site officiel de Raspberry pi:
https://www.raspberrypi.com/software/

Créer votre compte et suivre les instructions d'installations pour que tout soit prêt. N'oubliez pas de vous connecter à l'internet. Assurez-vous d'avoir accès à votre compte GitHub et ce projet à travers le Raspberry pi.
Maintenant que ceci est fait, installez "Visual studio code", l’éditeur de code source qui sera utilisé. Vous pouvez faire ceci en ouvrant le terminal et en entrant ces deux commandes une après l'autre. 
```
sudo apt update
sudo apt install code
```
Vous pouvez maintenant ouvrir l'application de programmation. Sur l'onglet à gauche, sélectionnez l'onglet le plus bas des extensions. Installez les extensions "SQLite", "SQLite Viewer", "Pylance", "Python" et "Python Debugger" pour le programme. 

### Schémas <a name="Schémas"></a>
#### Diagramme de pièces <a name="pièces"></a>
Voici le diagramme de pièces:
![Image2](https://github.com/WishPib/Aquaponie/assets/157630823/79346b21-7e17-4f20-8a16-67164ce68d67)


#### Diagramme de classes <a name="classes"></a>
Voici le diagramme de classes:
![Image3](https://github.com/WishPib/Aquaponie/assets/157630823/857fc46d-aedd-4536-8c7c-0c42c41bce10)

#### Diagramme de cas d'utilisation <a name="utilisation"></a>
Voici le diagramme de cas d'utilisation:
![Image1](https://github.com/WishPib/Aquaponie/assets/157630823/b8f7ab0f-fb2e-4129-9101-3ffc8ea9011e)
Nom: Retirer de l'information. 

Données d'entrée: Ce cas commence dès que l'utilisateur du système Aquaponie accède au site Web. Il a l'option de cliquer sur plusieurs boutons ayant différentes fonctionnalités spécifiées. 

Scénario Principal:  
L'utilisateur observe les dernières données récoltées par les capteurs dans le menu principal, ainsi que la date précise à laquelle celles-ci ont été mises à jour.  
L'utilisateur clique sur "actualiser" pour mettre à jour les données pour avoir le compte-rendu le plus récent de son projet d'aquaponie. 
Le système fournit un tableau d'informations mises à jour à l'instant, s'il est temps de nourrir les poissons ou d'ajuster le niveau d'eau, le système affichera un message concernant cela 
L'utilisateur fait une demande d'enregistrement de données en cliquant sur le bouton "enregistrer" 
Le système demande à l'utilisateur de façon d'enregistrer les données obtenues en forme de base de données. 
Scénario alternatif:  
1a. L'utilisateur clique sur "valeurs attendues" pour avoir accès aux intervalles de valeurs dans lesquels devraient se trouver les mesures fournies par les différents capteurs.  
2a. Le système affiche les intervalles 
 
Scénario alternatif: 
2a. Le client entre le mode d'opérations manuel en cliquant sur le bouton "override" 
3a. Le système affichera une nouvelle page, donnant l'option de 3 boutons; un interrupteur pour allumer/éteindre la pompe, un bouton pour mettre à jour le Raspberry Pi et un "killswitch" pour éteindre la pompe et le Raspberry 

### Guide d'utilisation <a name="Guide"></a>
Connectez tous les capteurs comme expliqué dans la section [Diagramme de pièces](#pièces). Prenez votre grand bac et collez le capteur de niveau d'eau IDUINO SE045 à l'intérieur du bord, à une position haute et pointant vers le bas dans le bac. Placez la pompe d'eau à l'extérieur du bac d'une manière qui permet qu'un des tube d'aller dans le bac et que l'autre attend à l'extérieur. Prenez vos plantes et mettez le capteur d'humidité dans la terre. Maintenant, remplissez le bac avec de l'eau jusqu'à ce que le niveau de l'eau touche le capteur du niveau d'eau et mettez les poissons dedans. Ensuite, mettez les plantes sur le bac, arrosez-les prématurement et placez le deuxième tube de la pompe qui était à l'extéreur dans une manière où l'eau qui sortira du tube arrosera les plantes. Puis, allumez la pile conntectée au système et connectez-vous le raspberry pi. Finalement, démarrez le programme comme c'est expliqué à la fin de la section [Installations à faire](#Installations) et vous pouvez vous déconnecter du raspberry pi après avoir confirmer que le système marche et que vous avez accès au site, mais n'oubliez pas de ne pas l'éteindre. Voilà, vous avez un système aquaponie automatisé. Le maintien des plantes et des poissons va dépendre de vous, car il varie selon lesquels vous avez choisis.

## Résultas <a name="Résultas"></a>
Alors, avec ce système, on est capable de déterminer l'humidité de la terre des plantes et si l'eau dans le bac a atteint un certain niveau et on peut obtenir ces informations à partir d'un site web où ces données sont affichées. Voici un exemple de la base de donnée qui sera obtenue pour transférer les données sur le site:

![Capture d’écran 2024-05-08 104033](https://github.com/WishPib/Aquaponie/assets/157630823/c147f363-ac04-45b9-b82f-4744f945b55c)

Puis, voici à quoi le site ressemble:

![site aquaponie](https://github.com/WishPib/Aquaponie/assets/157630823/8515e632-709e-4ae4-8a4a-2238615e9554)

## Discussion <a name="Discussion"></a> 
Alors, pour condenser notre projet en une phrase, on a réussi à manipuler automatiquement une pompe d'eau selon le niveau de l'eau, à capter l'humidité dans la terre des plantes dans un système d'aquaponie et d'afficher l'état de ce système sur un site web qu'on a créé. Parlons maintenant des prochaines étapes qu'on planifiait de faire si on le pouvait. La première chose qu'on aurait fait, c'est d'utiliser plus de capteurs et d'améliorer notre capteur de niveau d'eau. Bien qu'ils n'étaient pas nécessaires, avoir un capteur de niveau d'eau qui envoie une donnée plus précise et des capteurs de lumière, température ou de pH serait bien, car il est toujours bien d'avoir plus de données. La deuxième chose qu'on aurait fait, c'est créer un distributeur de nourriture automatique pour les poissons, quelque chose qui permettrait de mettre de la nourriture de poissons dans le bac à un temps régulier choisi par l'utilisateur, qui l'avertira sur le site si le distributeur commence à devenir vide et qui sera moins cher qu'un de ces distributeurs qui peuvent être trouvés dans des magasins. Finalement, on aurait testé notre système avec des vrais plantes et des vrais poissons, juste pour confirmer l'efficacité du système. Bien que nous n'avions pas eu la chance de faire ces améliorations, vous pouvez les considérez ces options comme des choses à ajouter vous-mêmes à votre projet.

## Conclusion <a name="Conclusion"></a>
Pour résumer, ce projet est notre manière d'automatiser un système d'aquaponie. Vous commencez par trouver le matériel que vous n'aviez pas, incluant un potager, un Raspberry pi qui est assez récent, une carte SD de minimum 16GB, un capteur de niveau d'eau IDUINO SE045, un capteur d'humidité de AZDelivery, une pompe d'eau DC DIY de INTLAB, un Ti-Cobbler Plus et des fils GPIO pour tout connecter. Après avoir installé le système d'exploitation sur le Raspberry pi et avoir complété toutes autres préparations, vous pouvez installer l'éditeur de code source "Visual studio code" et les extensions nécessaires pour le programme. Connectez tous vos capteurs comme montré dans les schémas et appliquez les dans votre potager ou jardin, puis vous pourriez contrôler le statut du système de n'importe où à partir du site web créer quand vous commenceriez le programme. Suivez nos instructions et comparez nos résultats avec les votres. Puis, voilà, une grande partie de votre main-d'œuvre se fait automatiquement et ce que vous faites manuellement n'est pas trop difficile.

### Autheurs <a name="Autheurs"></a>
Raphaël Hoffmann, Raphaël Charabaty, Shunyi Wang et Victor Alexandre Frings-Morales sont tous des étudiants dans le programme de Sciences, informatique et mathématique au Collège Bois de Boulogne à Montréal. Ils ont fait ce projet d’aquaponie pour leur dernier cours de programmation dans leur programme, le cours de projet d’intégration en sciences informatiques et mathématiques.
