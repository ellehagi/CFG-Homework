import requests
from pprint import pprint as pp
#pokemon_number = input("What is the Pokemon's ID? ")
pokemon_ids_list = [1,2,3,4,5,6]

url = 'https://pokeapi.co/api/v2/pokemon/'

for i in pokemon_ids_list:
    request = url+str(i)
    response = requests.get(request)
    data = response.json()
    #print(data)
    name = data['name']
    moves = data['moves']
    print(f'Name: {name}')
    print('Moves:')
    for move in moves:
        print('\t' + move['move']['name'])