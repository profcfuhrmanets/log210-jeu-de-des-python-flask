# Squelette pour un API simple dans Python et Flask 1.x

Ce squelette est proposé pour commencer les projets en LOG210. Il possède les qualités suivantes:

- il est simple pour les débutants en LOG210 
  - il n'y a pas de framework pour le front-end ni pour la persistance, mais ça n'empêche pas d'ajouter ces dimensions.
  - il est seulement [REST niveau 1](https://restfulapi.net/richardson-maturity-model/#level-one), mais ça n'empêche pas de modifier l'API pour qu'il soit [REST niveau 3](https://restfulapi.net/richardson-maturity-model/#level-three).
- il est orienté objet (avec Python)
- il contient des tests pour l'API (avec `unittest`)
- il fait une séparation entre les couches présentation et domaine, selon la méthodologie de conception du cours LOG210 (Larman)
- il fonctionne sur Windows 10 (et probablement d'autres systèmes d'exploitation avec Python 3 en `venv`)  

> **NB**: Il existe également [une variante de ce squelette pour Node.js/Express](https://github.com/profcfuhrmanets/log210-jeu-de-des-node-express-ts).

## D'où vient l'idée de base pour ce squelette?

Le code original vient d'un dépôt Git avec un excellent tutoriel dans son README à https://github.com/mjhea0/flaskr-tdd. Ce dernier utilise même une base de données, mais il ne fait pas la
séparation entre les couches de présentation et de domaine. C'est normal, puisque le problème présenté dans le tutoriel est simple (une seule classe du domaine). Pourtant, pour les systèmes complexes (avec un nombre important de classes du domaine),
il vaut mieux faire la séparation de ces couches. Donc, j'ai adapté le tutoriel pour démontrer une façon de faire qui soit compatible avec la méthodologie enseignée dans le cours.

Dans le cadre du cours [LOG210 de l'ÉTS](https://www.etsmtl.ca/Programmes-Etudes/1er-cycle/Fiche-de-cours?Sigle=log210), nous utilisons la méthodologie documentée par [Craig Larman dans son livre *Applying UML and Patterns*](http://www.craiglarman.com/wiki/index.php?title=Book_Applying_UML_and_Patterns). Ce livre documente beaucoup de principes avec des exemples en Java, qui n'est plus autant à la mode comme à l'époque où le livre a été écrit.

Pourtant, il est encore possible de suivre cette méthodologie avec des technologies modernes comme Python. Cependant, il n'est pas évident de trouver des exemples de ces technologies qui respectent les éléments clés de la méthodologie de Larman: la séparation des couches (présentation, domaine) avec les opérations système et les classes du domaine. Par exemple, sur StackOverflow on trouve des questions comme [How to split models.py into several files](https://stackoverflow.com/q/6336664/1168342), un problème d'évolutivité pour beaucoup de frameworks populaires.

Ce squelette montre ces aspects importants, dans le contexte du *Jeu de dés*, qui est l'exemple utilisé dans le chapitre 1 du livre du cours. Nous avons modifié l'exemple pour le rendre un peu plus complexe (plusieurs opérations système). Les diagrammes (faits avec [PlantUML](https://stackoverflow.com/questions/32203610/how-to-integrate-uml-diagrams-into-gitlab-or-github)) sont présentés plus bas dans la partie Artefacts.

L'IDE [PyCharm](https://www.jetbrains.com/pycharm/), dont il y a possibilité d'avoir une license pour la version professionnelle en tant qu'étudiant à l'ÉTS, est très utile parce qu'il offre un support pour le framework Flask et les tests. Mais il n'est pas nécessaire avec ce squelette.

## Pour utiliser ce squelette

1. Installer Python 3 (en mode local sur Windows, par exemple)

    [Python 3.6](https://www.python.org/downloads/release/python-360/) doit être installé, Il est téléchargeable à [http://www.python.org/download/](http://www.python.org/download/)

1. Fork/Clone/Dezipper ce dépôt

1. Créer et activer l'environnement virtuel [venv](https://docs.python.org/3/library/venv.html). 

    `venv` est utilisé pour créer un environnement isolé, une pratique importante pour le développement avec Python. Plus on fait de projets différents (avec leur dépendances différentes), plus c'est difficile d'isoler les dépendances sans des environnements virtuels.
    ```bash
    $ cd <répertoire_du_projet>
    $ python -m venv env
    $ source env/Scripts/activate
    ```
    Sur un autre système d'exploitation (Linux?) activer l'environnement virtuel ainsi:
    ```sh
    $ source env/bin/activate
    ```
    > **NB**: La première commande `$ python -m venv env` n'est nécessaire qu'une seule fois pour créer l'environnement virtuel.

    > **NB**: L'activation de l'environnement virtuel s'indique par le mot "env" avant le $ dans le terminal - (env)$. Pour quitter cet environnement, utiliser la commande `deactivate`. Ne pas oublier de l'activer de nouveau avant de continuer à travailler sur le projet.

1. Installer Flask (ici j'utilise git bash sous Windows 10):

    ```bash
    (env)$ pip install flask==1.0.2
    ```

1. Configurer les variables d'environnement pour Flask:
    ```bash
    (env)$ export FLASK_APP=jeu_de_des/app.py
    (env)$ export FLASK_ENV=development
    (env)$ export FLASK_DEBUG=0
    ```

1. Exécuter le serveur:
    ```bash
    (env)$ python -m flask run
    ```

    Vous devriez voir:
    ```
     * Serving Flask app "jeu_de_des/app.py"
     * Environment: development
     * Debug mode: off
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    ```

    Le serveur sera accessible sur votre machine à http://127.0.0.1:5000/ et vous devriez voir un écran comme ceci:

    ![Jeu de dés capture d'écran](https://github.com/profcfuhrmanets/log210-jeu-de-des-python-flask/raw/master/docs/Jeu_de_d%C3%A9s_index.png?s=50)

1. Exécuter les tests (il n'est pas nécessaire de lancer le serveur d'abord, car les tests lancent le serveur au besoin):
    ```bash
    (env)$ python jeu_de_des/app-test.py
    ```

    Le résultat des tests est comme ceci:
    ```
    ..........
    ----------------------------------------------------------------------
    Ran 10 tests in 0.096s

    OK
    ```

    Chaque `.` représente un test qui a passé.    

## Développement piloté par les tests (TDD)

![États du TDD](http://www.plantuml.com/plantuml/proxy?src=https://raw.githubusercontent.com/profcfuhrmanets/log210-jeu-de-des-python-flask/master/docs/tdd.puml)

Le développement piloté par les tests (Test-Driven Development, TDD) est une façon de développer des logiciels en commençant par les tests. Il y a plusieurs avantages de cette façon de faire et ce squelette supporte la méthodologie.

Le TDD suit un cycle particulier, comme vous pouvez voir à l'image plus haut:

1. Écrire un nouveau test
2. Exécuter le test (qui échouera)
3. Écrire juste assez de code pour faire passer le test
4. Refactoriser le code (et les tests) au besoin et recommencer

> Il y a des tests pour tous les appels de l'API du serveur web, mais on devrait
également faire des tests pour les autres classes (p.ex. au niveau test unitaire 
des classes du domaine).

## Couplage souhaitable entre la couche Présentation et la couche Domaine

Dans un bon design (selon Larman), on évite que la couche Présentation ait la responsabilité de gérer les évènements système (opérations système). Larman présente dans son livre un exemple avec un JFrame (en Java Swing) à la figure F16.24. On l'adapte ici au contexte d'un service Web avec Flask (Python):

![Diagramme de séparation des couches avec une opération système envoyée au contrôleur GRASP](http://www.plantuml.com/plantuml/proxy?fmt=svg&src=https://raw.githubusercontent.com/profcfuhrmanets/log210-jeu-de-des-python-flask/master/docs/figure-f16.24-web-flask.puml?cacheinc=1)

Dans la figure ci-dessus, l'objet `:JeuDeDes` (qui est un objet en dehors de la couche présentation) reçoit l'opération système `demarrerJeu(nom)` selon le principe GRASP Contrôleur. Ce squelette respecte cette séparation.

## Artefacts d'analyse et de conception

### Cas d'utilisation

#### Jouer aux dés

1. Le Joueur demande à démarrer le jeu en s'identifiant. 
1. Le Joueur demande à lancer les dés. 
1. Le Système affiche le nom du joueur et le résultat du lancer des dés, ainsi que le nombre de lancers et le nombre de fois que le Joueur a gagné. Pour un lancer, si le total est égal à sept, le Joueur a gagné. Dans tous les autres cas, il a perdu. 

*Le Joueur répète l’étape 3 jusqu’à ce qu’il ait fini.*

4. Le Joueur demande à terminer le jeu.
1. ~~Le Système affiche un tableau de bord avec les noms des joueurs et le ratio des parties gagnées (nombre de fois gagné / nombre de lancers).~~

### Diagramme de cas d’utilisation

![Diagramme de cas d'utilisation](http://www.plantuml.com/plantuml/proxy?fmt=svg&src=https://raw.githubusercontent.com/profcfuhrmanets/log210-jeu-de-des-node-express-ts/master/docs/dcu.puml?cacheinc=5)

### Modèle du domaine

![Diagramme de classe du Modèle du domaine](http://www.plantuml.com/plantuml/proxy?fmt=svg&src=https://raw.githubusercontent.com/profcfuhrmanets/log210-jeu-de-des-node-express-ts/master/docs/mdd.puml?cacheinc=5)

### Diagramme de séquence système (DSS)

![Diagramme de séquence système](http://www.plantuml.com/plantuml/proxy?fmt=svg&src=https://raw.githubusercontent.com/profcfuhrmanets/log210-jeu-de-des-node-express-ts/master/docs/dss-jouer.puml?cacheinc=5)

### Réalisations de cas d'utilisation (RDCU)

> **NB**: En Python, on réalise la structure de données `Map` (de Larman) avec un [Dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries).

![Diagramme de séquence, demarrerJeu](http://www.plantuml.com/plantuml/proxy?fmt=svg&src=https://raw.githubusercontent.com/profcfuhrmanets/log210-jeu-de-des-node-express-ts/master/docs/rdcu-demarrerJeu.puml?cacheinc=5)

![Diagramme de séquence, demarrerJeu](http://www.plantuml.com/plantuml/proxy?fmt=svg&src=https://raw.githubusercontent.com/profcfuhrmanets/log210-jeu-de-des-node-express-ts/master/docs/rdcu-jouer.puml?cacheinc=5)

![Diagramme de séquence, demarrerJeu](http://www.plantuml.com/plantuml/proxy?fmt=svg&src=https://raw.githubusercontent.com/profcfuhrmanets/log210-jeu-de-des-node-express-ts/master/docs/rdcu-terminerJeu.puml?cacheinc=5)
