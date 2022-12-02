import requests

ENDPOINT_POKE = 'https://pokeapi.co/api/v2/pokemon/charmander'

response = requests.get(ENDPOINT_POKE)

response = response.json()

abilities = response['abilities'][0]
ability_name = abilities['ability']['name']

# print(response['abilities'])

if 'blaze' in ability_name:
    print('Y')
else:
    print('N')

