import json

# procura = input("Digite: ")

local = "Programming_Languages_Extensions.json"

arq_jso = open(local, "r")

# Carregar arquivos json
arq_jso = json.load(arq_jso)


while True:

    procura = input("Digite: ")
    for i in range(len(arq_jso)):
        if "extensions" in arq_jso[i]:
            if procura in arq_jso[i]["extensions"]:
                print(arq_jso[i]["name"])
