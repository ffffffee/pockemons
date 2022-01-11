import requests
req=requests.get("https://w-dog.ru/wallpapers/9/15/458745441613494/vajoming-ssha-grand-teton-nacionalnyj-park-snejk-river-grand-titon-nacionalnyj-park-zakat-oblaka-vecher-gory-pole-cvety-zelen-les-derevya-sosny.jpg")
content=req.content
img=open("img.jpg","wb")
img.write(content)
img.close()