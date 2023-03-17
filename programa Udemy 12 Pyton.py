import requests
import json
import pprint

r = requests.get("https://opentdb.com/api.php?amount=1&category=12&difficulty=easy&type=multiple")
r.status_code

print(r.text)

type(r.text)

pregunta = json.load(r.text)
pprint.pprint(pregunta)
pregunta['results'][0]['category']

persona = ['Name': 'John','Age': 30 ] 
persona_json = json.dumps(persona) 