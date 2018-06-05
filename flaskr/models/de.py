from random import randint

class De():

    def __init__(self):
        self.valeur = 0
        self.brasser()

    def brasser(self):
        self.valeur = randint(1, 6)
        return self.valeur
