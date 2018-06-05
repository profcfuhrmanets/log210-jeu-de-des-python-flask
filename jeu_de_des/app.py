# imports
import json
import os

from flask import Flask, render_template, flash

# get the folder where this file runs
from markupsafe import Markup

# Contrôleur(s) GRASP appelé(s) dans le MDD
from jeu_de_des.models.jeu_de_des import JeuDeDes

# basedir = os.path.abspath(os.path.dirname(__file__))

# configuration
# DATABASE = 'flaskr.db'
DEBUG = True
SECRET_KEY = 'my_precious'
# USERNAME = 'admin'
# PASSWORD = 'admin'

# define the full path for the database
# DATABASE_PATH = os.path.join(basedir, DATABASE)

# database config
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
# SQLALCHEMY_TRACK_MODIFICATIONS = False


def create_app(config_name):
    """

    :type config_name: str
    """
    # create app
    app = Flask(__name__)
    app.config.from_object(__name__)
#    db = SQLAlchemy(app)

    # Init contrôleur GRASP
    jeu = JeuDeDes()

    @app.route('/api/v1/jeu/demarrerJeu/<nom>', methods=['GET'])
    def new_game(nom):

        try:
            # appeler le contrôleur GRASP
            joueur = jeu.demarrer_jeu(nom)
            resp = json.dumps({'nom': joueur.nom})
            stat = 201
            flash('Nouveau jeu pour ' + nom)
        except ValueError as e:
            resp = json.dumps({'erreur': str(e)})
            stat = 400
            flash(str(e))
        finally:
            response = app.response_class(
                response=resp,
                status=stat,
                mimetype='application/json'
            )

        return response

    @app.route('/api/v1/jeu/jouer/<nom>', methods=['GET'])
    def play_game(nom):

        try:
            # appeler le contrôleur GRASP
            result = jeu.jouer(nom)
            r_json = json.loads(result)
            resp = json.dumps(
                {'message': 'Success',
                 'result': r_json}
            )
            stat = 200
            flash(Markup('Résultat pour ' + nom + ':<br>' + str(r_json['v1']) + ' + ' + str(r_json['v2']) + ' = ' + str(r_json['somme'])))
        except ValueError as e:
            resp = json.dumps({'erreur': str(e)})
            stat = 400
            flash(str(e))
        finally:
            response = app.response_class(
                response=resp,
                status=stat,
                mimetype='application/json'
            )

        return response

    @app.route('/api/v1/jeu/terminerJeu/<nom>', methods=['GET'])
    def end_game(nom):

        try:
            # appeler le contrôleur GRASP
            result = jeu.terminer_jeu(nom)
            resp = json.dumps(
                {'message': 'Success',
                 'result': json.loads(result)}
            )
            stat = 200
            flash('Jeu terminé pour ' + nom)
        except ValueError as e:
            resp = json.dumps({'erreur': str(e)})
            stat = 400
            flash(str(e))
        finally:
            response = app.response_class(
                response=resp,
                status=stat,
                mimetype='application/json'
            )

        return response

    @app.route('/')
    def index():
        """Searches the map of players then displays them."""
        joueurs = jeu.joueurs.values()
        return render_template('index.html', joueurs=joueurs)

    if __name__ == '__main__':
        app.run()

    return app

