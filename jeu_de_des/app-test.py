import unittest
import json

from jeu_de_des.app import create_app

TEST_NOM1 = 'Jean-Marc'


class GameStartTest(unittest.TestCase):

    def setUp(self):
        """Start the app before each test"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()

    def test_start(self):
        """testing creation of game for a new player"""
        response = self.client.get('/api/v1/jeu/demarrerJeu/' + TEST_NOM1, content_type='html/text')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data)['nom'], TEST_NOM1)

    def test_start_null_name(self):
        """testing creation of game for a new player"""
        response = self.client.get('/api/v1/jeu/demarrerJeu/', content_type='html/text')
        self.assertEqual(response.status_code, 404)

    def test_duplicate_start(self):
        """testing creation of game for an existing player"""
        response = self.client.get('/api/v1/jeu/demarrerJeu/' + TEST_NOM1, content_type='html/text')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data)['nom'], TEST_NOM1)

        response2 = self.client.get('/api/v1/jeu/demarrerJeu/' + TEST_NOM1, content_type='html/text')
        self.assertEqual(response2.status_code, 400)
        self.assertTrue('existe déjà' in json.loads(response2.data)['erreur'])


class GamePlayTest(unittest.TestCase):

    def setUp(self):
        """Start the app before each test"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()

    def test_jouer_joueur_nonexistant(self):
        """testing play of game for an non-existing player"""
        response = self.client.get('/api/v1/jeu/jouer/' + TEST_NOM1, content_type='html/text')
        self.assertEqual(response.status_code, 400)
        self.assertTrue('n\'existe pas' in json.loads(response.data)['erreur'])

    def test_jouer(self):
        """testing play of game for an existing player"""
        response_0 = self.client.get('/api/v1/jeu/demarrerJeu/' + TEST_NOM1, content_type='html/text')
        response = self.client.get('/api/v1/jeu/jouer/' + TEST_NOM1, content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['result']['nom'], TEST_NOM1)

    def test_jouer_many_times(self):
        """testing multiple plays of game for an existing player"""
        response_0 = self.client.get('/api/v1/jeu/demarrerJeu/' + TEST_NOM1, content_type='html/text')
        for i in range(20):
            response = self.client.get('/api/v1/jeu/jouer/' + TEST_NOM1, content_type='html/text')
            r_data_json = json.loads(response.data)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(r_data_json['result']['nom'], TEST_NOM1)
            self.assertEqual(r_data_json['result']['lancers'], i+1)
            self.assertIn(r_data_json['result']['v1'], range(1, 7))
            self.assertIn(r_data_json['result']['v2'], range(1, 7))
            self.assertEqual(r_data_json['result']['somme'], r_data_json['result']['v1']+r_data_json['result']['v2'])

    def test_jouer_null_name(self):
        """testing creation of game for a new player"""
        response = self.client.get('/api/v1/jeu/jouer/', content_type='html/text')
        self.assertEqual(response.status_code, 404)


class GameEndTest(unittest.TestCase):

    def setUp(self):
        """Start the app before each test"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()

    def test_terminer_jeu(self):
        """testing ending of game for an existing player"""
        response_0 = self.client.get('/api/v1/jeu/demarrerJeu/' + TEST_NOM1, content_type='html/text')
        response_1 = self.client.get('/api/v1/jeu/jouer/' + TEST_NOM1, content_type='html/text')
        response = self.client.get('/api/v1/jeu/terminerJeu/' + TEST_NOM1, content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['result']['nom'], TEST_NOM1)

    def test_terminer_jeu_joueur_nonexistant(self):
        """testing ending of game for an existing player"""
        response = self.client.get('/api/v1/jeu/terminerJeu/' + TEST_NOM1, content_type='html/text')
        self.assertEqual(response.status_code, 400)
        self.assertTrue('n\'existe pas' in json.loads(response.data)['erreur'])

    def test_terminer_null_name(self):
        """testing creation of game for a new player"""
        response = self.client.get('/api/v1/jeu/terminerJeu/', content_type='html/text')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
