import requests
from pprint import pprint
from get_token import token
_print = print
print = pprint

url = 'http://?????????????/modelos'

headers = {
    'Authorization': token
}

response = requests.get(url=url, json=modelo_data, headers=headers)

if response.status_code >= 200 and response.status_code <= 299:
    # Sucesso
    print(response.status_code)
    print(response.reason)

    response_data = response.json()
    for modelo in response_data:
        print(carro['modelo'])

else:
    # Erros
    print(response.status_code)
    print(response.status_reason)
    print(response.status_text)