import json

# procura = input("Digite: ")

local = "Programming_Languages_Extensions.json"

arq_jso = open(local, "r")

# Carregar arquivos json
arq_jso = json.load(arq_jso)

print("Digite o final do formato junto com o ponto, exemplo '.p'")
print("Type the ending, the format with just the dot, example '.p'\n")


while True:
    c = 0
    achou = False
    procura = input("Digite: ")
    for i in range(len(arq_jso)):

        if "extensions" in arq_jso[i]:
            if procura in arq_jso[i]["extensions"]:
                print(arq_jso[i]["name"])
                achou = True

    # Se não achou
    if achou != True:
        print("Não achou nenhum formato.")
        print("Did not find any format.")
