import requests
from pprint import pprint
from get_token import token
_print = print
print = pprint

url = 'http://?????????????/modelos/??'

headers = {
    'Authorization': token
}

modelo_data = {
    'modelo': '??????',
    'velocidade_max': '??????',
    'motor': '??????',
    'marca': '??????'
}

response = requests.put(url=url, json=modelo_data, headers=headers)

if response.status_code >= 200 and response.status_code <= 299:
    # Sucesso
    print(response.status_code)
    print(response.status_reason)

    response_data = response.json()
    print(response_data)

else:
    # Erros
    print(response.status_code)
    print(response.status_reason)
    print(response.status_text)
