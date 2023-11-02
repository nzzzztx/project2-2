import requests

api_key = 'c3366f5c-665c-4f2d-8b37-3b9df48d0128'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

# print(definitions)

for definition in definitions:
    print(definitions)