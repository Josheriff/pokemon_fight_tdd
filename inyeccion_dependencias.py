def funcion_dos():
    return 2

def funcion_tres():
    return 3


def multiplica_la_funcion(otra_funcion):
    return otra_funcion() * 2

print(multiplica_la_funcion(funcion_dos))
print(multiplica_la_funcion(funcion_tres))

import requests

class Inyection:
    def bring_pokemon(self):
        pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/ditto/')
        return pokemon.json()


inyection = Inyection()
print(inyection.bring_pokemon())