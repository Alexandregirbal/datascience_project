# Manuel d'utilisation

## Prérequis
* Si vous utilisez un compte gmail il faut désactiver une sécurité sur votre boite mail: **Less secure app access**.

* Si vous utilisez un compte outlook (hotmail, live ...) il faut décommenter la ligne 45 du fichier `main.py`.

## Installation et lancement
1. Clonez ce projet sur votre machine.
2. Si vous souhaitez conserver vos credentials en local créez un fichier "config.py" qui est placé à la racine du projet contenant les lignes suivantes (pas d'inquiétude ce fichier est ignoré par git :wink:) :
            
        username = "yourEmail"
        password = "yourPassword"
        
3. Installez python 3 sur votre machine
4. Installez les librairies nécessaires
    
        pip3 install pandas wordcloud matplotlib nltk numpy pprintpp datetime imapclient pyzmail36

5. Exécutez la commande suivante dans un terminal, à la racine du projet:

        python3 main.py

6. Vous n'avez plus qu'à suivre les instructions, bonne analyse ! :grin:


## Notes supplémentaires:

* Une fois une fichier csv généré avec une adresse email vous n'aurez plus à récupérer les données en ligne.
* Vous pouvez configurer certains paramètres comme la date ou le sender dans le fichier `devConfig.py`