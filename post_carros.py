import requests
from pprint import pprint
_print = print
print = pprint

url = 'http://?????????????'

carros_data = [
    {
        'modelo': 'HB20',
        'velocidade_max': '180.0',
        'motor': '1.6',
        'marca': 'Hyundai'
    },

    {
        'modelo': 'XC60',
        'velocidade_max': '175.0',
        'motor': '2.0',
        'marca': 'Volvo'
    },

    {
        'modelo': 'Compass',
        'velocidade_max': '195.0',
        'motor': '2.0',
        'marca': 'Jeep'
    },

    {
        'modelo': 'Fox',
        'velocidade_max': '160.0',
        'motor': '1.6',
        'marca': 'Volkswagen'
    },

    {
        'modelo': 'Evoque',
        'velocidade_max': '185.0',
        'motor': '2.0',
        'marca': 'Land Rover'
    },

    {
        'modelo': 'Polo',
        'velocidade_max': '195.0',
        'motor': '1.6',
        'marca': 'Volkswagen'
    }


]

response = requests.post(url=url, json=carros_data)

if response.status_code >= 200 and response.status_code <= 299:
    # Sucesso
    print(response.status_code)
    print(response.status_reason)
    print(response.json())

else:
    # Erros
    print(response.status_code)
    print(response.status_reason)
    print(response.status_text)
