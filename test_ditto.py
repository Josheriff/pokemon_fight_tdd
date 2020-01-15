##### codigo prod ######
class Pokemon:
    def __init__(self, requests):
        self.requests = requests
    def get_ditto(self):
        ditto = self.requests.get('https://pokeapi.co/api/v2/pokemon/ditto/')
        name = ditto.json()
        name = name['forms'][0]['name']
        return name


##### test #######
import unittest
from unittest.mock import MagicMock

tocho_json = {'forms': [{
            'name': 'ditto',
            'url': 'https://pokeapi.co/api/v2/pokemon-form/132/'
            }]}

class TestPokemons(unittest.TestCase):
    def test_check_ditto(self):
        my_requests = MagicMock()
        pokemon = Pokemon(my_requests)
        
        pokemon.get_ditto()

        my_requests.get.assert_called_once_with('https://pokeapi.co/api/v2/pokemon/ditto/')

    def test_name_ditto_is_properly_parsed(self):
        my_requests = MagicMock()
        fake_json = MagicMock()
        fake_json.json.return_value= tocho_json
        pokemon = Pokemon(my_requests)
        my_requests.get.return_value = fake_json

        ditto_name = pokemon.get_ditto()

        assert ditto_name == 'ditto'