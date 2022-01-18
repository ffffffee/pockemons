import requests

pokemons = {}


class Pokemon:
    def __init__(self, json):
        self.name = json["name"]
        self.height = json["height"]
        self.abilities = []
        for i in range(len(json["abilities"])):
            self.abilities.append(json["abilities"][i]["ability"]["name"])

    def get(self):
        print("name:", self.name)
        print("height:", self.height)
        print("abilities:", ", ".join(self.abilities))


while True:
    command = input()
    if command == "get":
        name_pokemon = input("Введите имя: ")
        if pokemons.get(name_pokemon):
            pokemons.get(name_pokemon).get()
        else:
            r = requests.get("https://pokeapi.co/api/v2/pokemon/" + name_pokemon)
            if r.status_code == 200:
                r = r.json()
                pokemons[name_pokemon] = Pokemon(r)
                pokemons[name_pokemon].get()
            elif r.status_code==404:
                print("Такого покемона не существует!")
            elif r.status_code==403:
                print("Вы забанены")
            else:
                print("хз")

    else:
        print("Такой команды не существует!")
