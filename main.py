import requests
import json

while True:
    command = input()
    if command == "add":
        req = requests.get("https://aws.random.cat/meow")
        r=requests.get(json.loads(req.text)["file"])
        content=r.content
        img=open("img.jpg","wb")
        img.write(content)
        img.close()
        print("nice")
