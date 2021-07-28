# Escape Game server in python

Ce projet est un travail personnel pour une utilisation personnelle. Il permet de facilement créer un server web pour un escape game.

## Installation

Il est basé sur [python3.7](https://python.org) ou plus.
Il a besoin de [django](https://www.djangoproject.com/) 3.2.5 (seul version testée).

Copier l'ensemble des fichiers et dossiers dans votre espace de travail,
Puis lancer la commande de démarage du serveur:
```batch
python manage.py runserver
```

Pour accerder au site, utiliser edge (version chromium) et aller sur 127.0.0.1:8000

Si vous voullez acceder à distance, utiliser la commande suivante:
```batch
python manage.py runserver [your ip]:80
```

Pour avoir votre ip:
windows: ipconfig
linux: ifconfig

## Utilisation

Une fois le serveur lancé, vous pouvez aller sur le site à partir d'un navigateur chromium (de préférance edge).
Que vous recharger la page, revenier sur les page d'avant ou ouvrer un autre navigateur, ce serra toujours la même page.

Le seul moyen pour réinitialiser l'avancement sur l'escape game, c'est de taper l'url suivante:
`127.0.0.1:8000/azertyuiop` si vous êtes sur la machine hôte
ou
`[your ip]/azertyuiop` si vous êtes en distant


## Configuration

Pour changer les enigmes, vous pouvez éditer le fichier 'config.json' se trouvant à la racine du dossier du projet.

La structure normale du fichier est la suivante:
```json
{
    "1":{"title":"un titre", "text":"l'intituler de l'enigme", "result":"la réponse"},
    "2":{...},
    "3":{...},
    ...
}
```
![image d'exemple](/images/img2.png)

Si jamais vous avez besoin de multiple line à la place d'une seule ligne de texte, vous pouvez les mettre dans une liste:
```json
{
    "5":{
        "title":"un titre",
        "text":[
            "ligne 1",
            "ligne 2",
            "ligne 3"
        ],
        "result": "la réponse"
    }
}
```

![image d'exemple](/images/img3.png)