import requests #se der erro colocar no terminal "pip install requests"

#-------------------------------CHAMADA API-----------------------------------
#Chamar a api para pegar all bodies info
allBodiesPositionLink = "https://api.le-systeme-solaire.net/rest/positions"
keyPosition = "d0bdbb18-bbfb-4735-802d-b672501baeb8"

headers = {
    "Authorization": f"Bearer {keyPosition}"
}

params = {
    "lon": -52.34,
    "lat": -31.77,
    "elev": 20,
    "datetime": "2026-10-01T16:00:00",
    "zone": -3
}

allBodiesPosition = requests.get(allBodiesPositionLink, headers=headers, params=params)

allBodiesPositionData = allBodiesPosition.json() #criando obj com as inf

#-------------------------------FUNÇÕES-----------------------------------
def funcao_hash(chave): #função pra mapear os id's (chave) pra hash
    soma = 0

    for caractere in chave:
        soma += ord(caractere)  #ord transforma letra em número
    return soma % tamanho       #posição na tabela hash

def inserir_body(body):
    chave = body["name"]
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

    #dicionário só com os dados que a gnt quer de cada corpo - parsing
    novo_body = {
        "name": body["name"],
        "ra": body["ra"],
        "dec": body["dec"],
        "az": body["az"],
        "alt": body["alt"],
    }

    nova_posicao = (posicao + i**2) % tamanho   #a nova posição é a que fez o loop parar
    tabelaHash[nova_posicao] = novo_body

    return colisoes

#-------------------------------MAIN-----------------------------------
#fator carga -> 554 corpos e no máximo 70% ocupação
# -> 554/m = 0,7 -> m = 791,43 -> hash com 792 posições

tamanho = 792
tabelaHash = [None] * tamanho
numColisoes = 0
qtdElementos = 0

#inserindo os corpos na hash
for body in allBodiesPositionData["positions"]:
    numColisoes += inserir_body(body)

#contando elementos inseridos pra calcular o fator de carga
for posicao in tabelaHash:
    if posicao is not None:
        qtdElementos += 1

fatorCarga = qtdElementos / tamanho
print("Fator de carga:", round(fatorCarga * 100, 2), "%") #arredondamos p 2 casas
print("Número de colisões no carregamento:", numColisoes)

print(tabelaHash[(ord('L')+ord('u')+ord('n')+ord('e')) % 792])