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
    #fórmula da sondagem quadrática (h + i^2) % tamanho (nesse caso 792)
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
#-------------------------------MAIN-----------------------------------
qtdElementosPlanetas = 0

#contando elementos inseridos pra calcular o fator de carga
for posicao in tabelaPlanetas:
    if posicao is not None:
        qtdElementosPlanetas += 1

fatorCargaPlanetas = qtdElementosPlanetas / tamanhoPlanetas
print("Fator de carga Planetas:", round(fatorCargaPlanetas * 100, 2), "%") #arredondamos p 2 casas
print("Número de colisões no carregamento:", numColisoesPlanetas)

print(tabelaPlanetas[32])


#PESSOAS ****************************************************************
#-------------------------------FUNÇÕES-----------------------------------
def funcao_hash_planetas(chave): #função pra mapear os id's (chave) pra hash
    soma = 0

    for caractere in chave:
        soma += ord(caractere)  #ord transforma letra em número
    return soma % tamanhoPessoas      #posição na tabela hash

def inserir_pessoa(pessoa):
    chave = pessoa["name"]
    posicao = funcao_hash_planetas(chave)

    #depois de achar a posição se houver colisão vamos fazer a sondagem quadrática
    i = 0
    colisoes = 0
    #fórmula da sondagem quadrática (h + i^2) % tamanho (nesse caso 792)
    #h nossa posição inicialmente calculada e i o número de tentativas que fizemos de 
    #achar um lugar vazio
    while tabelaPessoas[(posicao + i**2) % tamanhoPessoas] is not None: 
        colisoes += 1
        i += 1

    #dicionário só com os dados que a gnt quer de cada corpo - parsing
    nova_pessoa = {
        "name": pessoa["name"],
        "mass": pessoa["mass"],
        "height": pessoa["height"],
        "gender": pessoa["gender"],
        "eye_color": pessoa["eye_color"]
    }

    nova_posicao = (posicao + i**2) % tamanhoPessoas   #a nova posição é a que fez o loop parar
    tabelaPessoas[nova_posicao] = nova_pessoa

    return colisoes

#-------------------------------CHAMADA API-----------------------------------
#fator carga -> 82 corpos e no máximo 70% ocupação
# -> 82/m = 0,7 -> m = 117 -> hash com 127 posições

tamanhoPessoas = 127
tabelaPessoas = [None] * tamanhoPessoas
numColisoesPessoas = 0

pessoasLink = "http://swapi.dev/api/people/"

while pessoasLink is not None:
    pessoasRespostas = requests.get(pessoasLink)
    pessoasDados = pessoasRespostas.json()

    for pessoa in pessoasDados["results"]:
        numColisoesPessoas += inserir_pessoa(pessoa)

    pessoasLink = pessoasDados["next"]
#-------------------------------MAIN-----------------------------------
qtdElementosPessoas = 0

#contando elementos inseridos pra calcular o fator de carga
for posicao in tabelaPessoas:
    if posicao is not None:
        qtdElementosPessoas += 1

fatorCargaPessoas = qtdElementosPessoas / tamanhoPessoas
print("Fator de carga Pessoas:", round(fatorCargaPessoas * 100, 2), "%") #arredondamos p 2 casas
print("Número de colisões no carregamento:", numColisoesPessoas)

print(tabelaPessoas[67])

#--------------------------Pesquisa e Listagem-----------------------------
def pesquisarPessoa(nomePessoa):
    for pessoa in tabelaPessoas:
        if(pessoa["name"] == nomePessoa):
            print(pessoa)
            return


#FUNÇÕES E MENU************************************************************
while True: #menu de navegação
    print("\nBem vindo ao sistema! O que gostaria de fazer?")
    print("1 - Pesquisar pessoa")
    print("2 - Pesquisar planeta")
    print("3 - Filtrar pessoas")
    print("4 - Filtrar planetas")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")
    
    match opcao:
        case "1":
            nomePessoa = input("Digite o nome da pessoa que está buscando:")
            pesquisarPessoa(nomePessoa)
        case "3":
            print("Por qual característica deseja filtrar?")

        case "0":
            print("Programa encerrado com sucesso!")
            break
        case _:
            print("Opção inválida, tente novamente.")