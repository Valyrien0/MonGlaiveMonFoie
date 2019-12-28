
Bot Discord pour jouer à Mon Glaive est Mon Foie.

Pour pouvoir lancer le bot il faut:
- avoir installer python3 avec le module discord.py
- créer un fichier .env dans le dossier de travail contenant votre token sous la forme DISCORD_TOKEN=...  (voir https://discordapp.com/developers/applications/)
- autoriser le bot sur un serveur


Les commandes utilisateurs:
!join, !leave : rejoindre et quitter la partie
!begin : débuter la partie

!roll : lancer les dés
!defend : s'interposer quand le Dieu attaque (pour le Héro et la Catin)
!give : distruer des gorgées TODO
!blow : souffler (pour le dragon)


Reste à faire:
Toutes les règles ne sont pas encore implémentées, il y a des TODO dans le code.
Mettre en place le système de distribution de gorgées.
Rendre le bot moins sensibles aux inputs des joueurs.

Eventuellement:
Rajouter les rôles Discord pour améliorer l'UI, on pourrait connaitre le rôle de chaque joueur, taguer des rôles, ... Y aurait des coleurs et tout ça ferait plus BDA !
Faire des stats sur chaque joueur pour savoir combien il a bu, combien de temps il est resté en prison...


Nota Bene:
Le code est pas hyper propre, mais c'est du python j'y peux rien !
Ok, j'avoue c'est à moitié en anglais, moitié en français...
Wesh.
