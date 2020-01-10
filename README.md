# Pokemon Fight TDD
Pequeña aplicación para aprender TDD

## Que hace:
Recibe 2 nombres, que serán los entrenadores pokemon.
2 Pokemon salen de la api pokeapi y se pelean entre ellos, y decimos el ganador.

## Como lo hace

 - Recibe los 2 nombres mediante api y los pone con la primera letra en mayuscula y el resto en minuscula, no admite espacios.
 - Hace una llamada a https://pokeapi.co/api/v2/pokemon/  y coge el valor `count` para saber el número máximo
 de pokemons actualmente.
 - Hace 2 llamadas a https://pokeapi.co/api/v2/{{numero-random-entre-1-y-maximoDePokemons}}
 - Los enfrenta
 - Pokemon 1 ataca a pokemon 2 con su ataque básico + un número random del 1 al 10
    Se le resta a la defensa del pokemon 2 y si es un número negativo, ese mismo número se le quita
    a la vida del pokemon 2 (`hp`)
- Lo mismo pero a la inversa.

El primer pokemon cuyo hp sea `0` o menor que `0`pierde, declarando al otro pokemon vencedor.
