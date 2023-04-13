#Test de integración: La conexión con la API de Ryanair se realiza
import requests
import unittest

class TestRyanairAPI(unittest.TestCase):
    def test_connection(self):
        url = "https://ryanair.p.rapidapi.com"
        headers = {"apikey": "e233a2be10msh8840ddf18877db9p19b37fjsnadbb89126e34"}
        response = requests.get(url, headers=headers)
        self.assertEqual(response.status_code, 200)

#Para ejecutarlo en la terminal: python -m unittest test_API.py
