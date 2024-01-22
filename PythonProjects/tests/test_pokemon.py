import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json'}

def test_get_trainers():
    """
    GET /trainers приходит кодом 200
    """
    response = requests.get(url=f'{URL}/trainers', params={'code':200}, timeout=5)
    assert response.status_code == 200, 'Unexpected status code'

def test_get_trainers_name():
    """
    GET /trainers имя тренера
    """
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id':3590}, timeout=5)
    assert response.json()['trainer_name'] == 'Ленивец Сид', ''