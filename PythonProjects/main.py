"""
Создание покемона
"""

import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json'}

body = {
    'trainer_token': '7bf1048ba74dcf64990afe79d94a992e',
    "email": "german@dolnikov.ru",
    "password": "Iloveqa1"
}

response = requests.post(url=f'{URL}/trainers/reg', json=body, headers=HEADER, timeout=5)
print(response)



HEADER = {'Content-Type': 'application/json', 'trainer_token': '7bf1048ba74dcf64990afe79d94a992e'}

body = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/002.png"
}

response = requests.post(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5)
print(response)


"""
Смена имени покемона
"""

HEADER = {'Content-Type': 'application/json', 'trainer_token': '7bf1048ba74dcf64990afe79d94a992e'}

body = {
    "pokemon_id": "28313",
    "name": "Тимон",
    "photo": "https://dolnikov.ru/pokemons/albums/002.png"
}

response = requests.put(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5)
print(response)


"""
Поймать покемона в покебол
"""

HEADER = {'Content-Type': 'application/json', 'trainer_token': '7bf1048ba74dcf64990afe79d94a992e'}

body = {
    "pokemon_id": "28313"
}

response = requests.post(url=f'{URL}/trainers/add_pokeball', json=body, headers=HEADER, timeout=5)
print(response)