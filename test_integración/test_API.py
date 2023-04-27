#Test de integración: La conexión con la API de Ryanair y Skyscanner se realiza
import requests
import unittest

class TestRyanairAPI(unittest.TestCase):
    def test_connection(self):
        url = "https://ryanair.p.rapidapi.com"
        headers = {"apikey": "6ae587a3bdmsh021d9a94bcaf13bp14ef7ejsn146886682b43"}
        response = requests.get(url, headers=headers)

        url = "https://skyscanner44.p.rapidapi.com"
        headers = {"apikey": "6ae587a3bdmsh021d9a94bcaf13bp14ef7ejsn146886682b43"}
        response = requests.get(url, headers=headers)
       

#Para ejecutarlo en la terminal: python -m unittest test_API.py
