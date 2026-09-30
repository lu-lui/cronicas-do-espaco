import requests #se der erro colocar no terminal "pip install requests"

#-------------------------------CHAMADA API-----------------------------------
#Chamar a api para pegar all bodies info
allBodiesLink = "https://api.le-systeme-solaire.net/rest/bodies/"
key = "748f851d-98b9-4e79-be35-dc33a4fb852e"

headers = {
    "Authorization": f"Bearer {key}"
}
allBodies = requests.get(allBodiesLink, headers=headers)

allBodiesData = allBodies.json() #criando obj com as inf

#Parsing - selecionando oq queremos guardar na hash
selectedData = []

for body in allBodiesData["bodies"]:
    newBody = {
        "id": body["id"],
        "name": body["name"],
        "englishName": body["englishName"],
        "mass": body["mass"],
        "gravity": body["gravity"],
        "sideralOrbit": body["sideralOrbit"],
        "discoveryDate": body["discoveryDate"],
        "avgTemp": body["avgTemp"],
        "bodyType": body["bodyType"]
    }
    selectedData.append(newBody)

#-------------------------------FUNÇÕES-----------------------------------
def funcao_hash(chave): #função pra mapear os id's (chave) pra hash
    soma = 0

    for caractere in chave:
        soma += ord(caractere)  #ord transforma letra em número
    return soma % tamanho       #posição na tabela hash

def inserir_body(body):
    chave = body["id"]
    posicao = funcao_hash(chave)

    #depois de achar a posição se houver colisão vamos fazer a sondagem quadrática
    i = 0
    colisoes = 0
    #fórmula da sondagem quadrática (h + i^2) % tamanho (nesse caso 792)
    #h nossa posição inicialmente calculada e i o número de tentativas que fizemos de 
    #achar um lugar vazio
    while tabelaHash[(posicao + i**2) % tamanho] is not None: 
        colisoes += 1
        i += 1

    nova_posicao = (posicao + i**2) % tamanho   #a nova posição é a que fez o loop parar
    tabelaHash[nova_posicao] = body

    return colisoes

#-------------------------------MAIN-----------------------------------
#fator carga -> 554 corpos e no máximo 70% ocupação
# -> 554/m = 0,7 -> m = 791,43 -> hash com 792 posições

tamanho = 792
tabelaHash = [None] * tamanho
numColisoes = 0
qtdElementos = 0

#inserindo os corpos na hash
for body in allBodiesData["bodies"]:
    numColisoes += inserir_body(body)

#contando elementos inseridos pra calcular o fator de carga
for posicao in tabelaHash:
    if posicao is not None:
        qtdElementos += 1

fatorCarga = qtdElementos / tamanho
print("Fator de carga:", round(fatorCarga * 100, 2), "%") #arredondamos p 2 casas
print("Número de colisões no carregamento:", numColisoes)
