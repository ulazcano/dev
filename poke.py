import requests
import json
 
url = "https://pokeapi.co/api/v2/pokemon/pikachu"
 
payload = ""
headers = {}

hola = requests.request("GET", url, headers=headers, data=payload)
jan= hola.json()

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(jan, f, ensure_ascii=False, indent=4)



for categoria in jan:
    print("**",categoria)
    for rr in jan[categoria]:
        print(rr)


