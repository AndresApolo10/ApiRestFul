import requests

ENDPOINT_POKEAPI = 'https://pokeapi.co/api/v2/pokemon/ditto'

response = requests.get(ENDPOINT_POKEAPI)

response = response.json()

abilities = response['abilities'][0]
ability_name = abilities['ability']['name']

if 'imposter' in ability_name:
    print('Y')
else:
    print('N')

