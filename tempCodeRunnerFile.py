import requests #se der erro colocar no terminal "pip install requests"

#PLANETAS ****************************************************************
#-------------------------------FUNÇÕES-----------------------------------
def funcao_hash_planetas(chave): #função pra mapear os id's (chave) pra hash
    soma = 0

    for caractere in chave:
        soma += ord(caractere)  #ord transforma letra em número
    return soma % tamanhoPlanetas       #posição na tabela hash

def inserir_planeta(planeta):
    chave = planeta["name"]
    posicao = funcao_hash_planetas(chave)

    #depois de achar a posição se houver colisão vamos fazer a sondagem quadrática
    i = 0
    colisoes = 0
    #fórmula da sondagem quadrática (h + i^2) % tamanho (nesse caso 89)
    #h nossa posição inicialmente calculada e i o número de tentativas que fizemos de 
    #achar um lugar vazio
    while tabelaPlanetas[(posicao + i**2) % tamanhoPlanetas] is not None: 
        colisoes += 1
        i += 1

    #dicionário só com os dados que a gnt quer de cada corpo - parsing
    novo_planeta = {
        "name": planeta["name"],
        "climate": planeta["climate"],
        "diameter": planeta["diameter"],
        "gravity": planeta["gravity"],
        "population": planeta["population"],
    }

    nova_posicao = (posicao + i**2) % tamanhoPlanetas   #a nova posição é a que fez o loop parar
    tabelaPlanetas[nova_posicao] = novo_planeta

    return colisoes

#-------------------------------CHAMADA API-----------------------------------
#fator carga -> 60 corpos e no máximo 70% ocupação
# -> 60/m = 0,7 -> m = 85 -> hash com 89 posições

tamanhoPlanetas = 89
tabelaPlanetas = [None] * tamanhoPlanetas
numColisoesPlanetas = 0

planetasLink = "http://swapi.dev/api/planets/"

while planetasLink is not None:
    planetasRespostas = requests.get(planetasLink)
    planetasDados = planetasRespostas.json()

    for planeta in planetasDados["results"]:
        numColisoesPlanetas += inserir_planeta(planeta)

    planetasLink = planetasDados["next"]
#-------------------------------MAIN PLANETAS-----------------------------------
qtdElementosPlanetas = 0

#contando elementos inseridos pra calcular o fator de carga
for posicao in tabelaPlanetas:
    if posicao is not None:
        qtdElementosPlanetas += 1

fatorCargaPlanetas = qtdElementosPlanetas / tamanhoPlanetas
print("Planetas__________________________________")
print("Fator de carga:", round(fatorCargaPlanetas * 100, 2), "%") #arredondamos p 2 casas
print("Número de colisões no carregamento:", numColisoesPlanetas)

#Personagem ****************************************************************
#-------------------------------FUNÇÕES-----------------------------------
def funcao_hash_personagens(chave): #função pra mapear os id's (chave) pra hash
    soma = 0

    for caractere in chave:
        soma += ord(caractere)  #ord transforma letra em número
    return soma % tamanhoPersonagens      #posição na tabela hash

def inserir_personagem(personagem):
    chave = personagem["name"]
    posicao = funcao_hash_personagens(chave)

    #depois de achar a posição se houver colisão vamos fazer a sondagem quadrática
    i = 0
    colisoes = 0
    #fórmula da sondagem quadrática (h + i^2) % tamanho (nesse caso 127)
    #h nossa posição inicialmente calculada e i o número de tentativas que fizemos de 
    #achar um lugar vazio
    while tabelaPersonagens[(posicao + i**2) % tamanhoPersonagens] is not None: 
        colisoes += 1
        i += 1

    linkHomeworld = personagem["homeworld"]
    respostaHomeWorld = requests.get(linkHomeworld)
    dadosHomeworld = respostaHomeWorld.json()
    nomeHomeWorld = dadosHomeworld["name"]

    #dicionário só com os dados que a gnt quer de cada corpo - parsing
    nova_personagem = {
        "name": personagem["name"],
        "mass": personagem["mass"],
        "height": personagem["height"],
        "gender": personagem["gender"],
        "eye_color": personagem["eye_color"],
        "homeworld": nomeHomeWorld
    }

    nova_posicao = (posicao + i**2) % tamanhoPersonagens   #a nova posição é a que fez o loop parar
    tabelaPersonagens[nova_posicao] = nova_personagem

    return colisoes

#-------------------------------CHAMADA API-----------------------------------
#fator carga -> 82 corpos e no máximo 70% ocupação
# -> 82/m = 0,7 -> m = 117 -> hash com 127 posições

tamanhoPersonagens = 127
tabelaPersonagens = [None] * tamanhoPersonagens
numColisoesPersonagem = 0

PersonagemLink = "http://swapi.dev/api/people/"

while PersonagemLink is not None:
    PersonagemRespostas = requests.get(PersonagemLink)
    PersonagemDados = PersonagemRespostas.json()

    for personagem in PersonagemDados["results"]:
        numColisoesPersonagem += inserir_personagem(personagem)

    PersonagemLink = PersonagemDados["next"]
#-------------------------------MAIN PERSONAGENS-----------------------------------
qtdElementosPersonagem = 0

#contando elementos inseridos pra calcular o fator de carga
for posicao in tabelaPersonagens:
    if posicao is not None:
        qtdElementosPersonagem += 1

fatorCargaPersonagem = qtdElementosPersonagem / tamanhoPersonagens
print("Personagens_____________________________")
print("Fator de carga:", round(fatorCargaPersonagem * 100, 2), "%") #arredondamos p 2 casas
print("Número de colisões no carregamento:", numColisoesPersonagem)
