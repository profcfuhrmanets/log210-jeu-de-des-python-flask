from jeu_de_des.models.de import De
from jeu_de_des.models.joueur import Joueur

import logging
import json

# logger = logging.Logger('catch_all')

class JeuDeDes():

    def __init__(self):
        """initialize the map of players"""
        self.joueurs = {}
        self.d1 = De()
        self.d2 = De()

    def demarrer_jeu(self, nom) -> Joueur:
        if nom in self.joueurs:
            err = "Joueur " + nom + " existe déjà."
            # logger.error(err)
            raise ValueError(err)

        # add to dictionary (map)
        joueur = Joueur(nom)
        self.joueurs[nom] = joueur

        return joueur

    def jouer(self, nom) -> str:
        if nom not in self.joueurs:
            err = "Joueur " + nom + " n'existe pas."
            # logger.error(err)
            raise ValueError(err)

        # get from dictionary (map)
        joueur = self.joueurs[nom]
        v1 = self.d1.brasser()
        v2 = self.d2.brasser()
        somme = v1 + v2
        joueur.lancer()
        if somme == 7:
            joueur.gagner()

        result = json.dumps(
            {'nom': nom,
             'somme': somme,
             'lancers': joueur.nb_lancers,
             'reussites': joueur.nb_lancers_gagnes,
             'v1': v1,
             'v2': v2,
             'message': "Vous avez " + ("gagné!!!" if somme == 7 else "perdu.")}
        )

        return result

    def terminer_jeu(self, nom) -> str:
        if nom not in self.joueurs:
            err = "Joueur " + nom + " n'existe pas."
            # logger.error(err)
            raise ValueError(err)

        # remove from dictionary (map)
        del self.joueurs[nom]

        result = json.dumps(
            {'nom': nom,
             'message': 'Merci d\'avoir joué.'}
        )

        return result
