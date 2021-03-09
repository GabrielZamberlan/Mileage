import requests
from pprint import pprint
_print = print
print = pprint

url = 'http://?????????????'

motor_data = {
    'motor': '????',
}

response = requests.post(url=url, json=motor_data)

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
