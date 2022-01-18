import requests

pokemons={}

class Pokemon:
    def __init__(self,json):
        self.name=json["name"]
        self.height = json["height"]
        self.abilities=[]
        for i in range(len(json["abilities"])):
            self.abilities.append(json["abilities"][i]["ability"]["name"])


    def check_status(self):
        r = requests.get("https://pokeapi.co/api/v2/pokemon/" + self.name)
        if r.status_code==200:
            return True
        return False
    def get(self):
        print("name:",self.name)
        print("height:",self.height)
        print("abilities:",", ".join(self.abilities))

while True:
    command=input()
    if command=="get":
        name_pokemon=input("Введите имя: ")
        if pokemons.get(name_pokemon):
            pokemons.get(name_pokemon).get()
        else:
            r = requests.get("https://pokeapi.co/api/v2/pokemon/" + name_pokemon)
            r=r.json()
            pokemons[name_pokemon]=Pokemon(r)
            pokemons[name_pokemon].get()
