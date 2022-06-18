import requests
from pprint import pprint as pp
#pokemon_number = input("What is the Pokemon's ID? ")
pokemon_ids_list = [1,2,3,4,5,6]

url = 'https://pokeapi.co/api/v2/pokemon/'
with open('pokemon.txt', 'w') as file:
    
    for i in pokemon_ids_list:
        request = url+str(i)
        response = requests.get(request)
        data = response.json()
        #print(data)
        name = data['name']
        moves = data['moves']
        #print(f'Name: {name}')
        file.write(f'Name: {name}\n')
        file.write('Moves:\n')
        #print('Moves:')
        for move in moves:
            #print('\t' + move['move']['name'])
            file.write('\t' + move['move']['name'] + '\n')

    