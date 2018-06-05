

class Joueur():

    def __init__(self, nom):
        """initialize player"""
        self.nom = nom
        self.nb_lancers = 0
        self.nb_lancers_gagnes = 0

    def lancer(self):
        self.nb_lancers += 1

    def gagner(self):
        self.nb_lancers_gagnes += 1

