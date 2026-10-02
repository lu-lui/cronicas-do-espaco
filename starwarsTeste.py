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
print("Planetas__________________________________")
print("Fator de carga:", round(fatorCargaPlanetas * 100, 2), "%") #arredondamos p 2 casas
print("Número de colisões no carregamento:", numColisoesPlanetas)

#Personagem ****************************************************************
#-------------------------------FUNÇÕES-----------------------------------
def funcao_hash_planetas(chave): #função pra mapear os id's (chave) pra hash
    soma = 0

    for caractere in chave:
        soma += ord(caractere)  #ord transforma letra em número
    return soma % tamanhoPersonagens      #posição na tabela hash

def inserir_personagem(personagem):
    chave = personagem["name"]
    posicao = funcao_hash_planetas(chave)

    #depois de achar a posição se houver colisão vamos fazer a sondagem quadrática
    i = 0
    colisoes = 0
    #fórmula da sondagem quadrática (h + i^2) % tamanho (nesse caso 792)
    #h nossa posição inicialmente calculada e i o número de tentativas que fizemos de 
    #achar um lugar vazio
    while tabelaPersonagens[(posicao + i**2) % tamanhoPersonagens] is not None: 
        colisoes += 1
        i += 1

    #dicionário só com os dados que a gnt quer de cada corpo - parsing
    nova_personagem = {
        "name": personagem["name"],
        "mass": personagem["mass"],
        "height": personagem["height"],
        "gender": personagem["gender"],
        "eye_color": personagem["eye_color"]
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
#-------------------------------MAIN-----------------------------------
qtdElementosPersonagem = 0

#contando elementos inseridos pra calcular o fator de carga
for posicao in tabelaPersonagens:
    if posicao is not None:
        qtdElementosPersonagem += 1

fatorCargaPersonagem = qtdElementosPersonagem / tamanhoPersonagens
print("Personagens_____________________________")
print("Fator de carga:", round(fatorCargaPersonagem * 100, 2), "%") #arredondamos p 2 casas
print("Número de colisões no carregamento:", numColisoesPersonagem)

#--------------------------Pesquisa e Listagem-----------------------------
def pesquisarPersonagem(nomePersonagem):
    for personagem in tabelaPersonagens:
        if personagem is not None:
            if(personagem["name"] == nomePersonagem):
                print("Nome: ", personagem["name"])
                print("Mass: ", personagem["mass"])
                print("Height: ", personagem["height"])
                print("Gender: ", personagem["gender"])
                print("Eye color: ", personagem["eye_color"])
                return

    print("Personagem não encontrada(o)")
    return

def pesquisarPlaneta(nomePlaneta):
    for planeta in tabelaPlanetas:
        if planeta is not None:
            if(planeta["name"] == nomePlaneta):
                print("Nome: ", planeta["name"])
                print("Climate: ", planeta["climate"])
                print("Diameter: ", planeta["diameter"])
                print("Gravity: ", planeta["gravity"])
                print("Population: ", planeta["population"])
                return

    print("Planeta não encontrado")
    return

def ler_intervalo():
    while True:
        minimo = input("Valor mínimo: ")
        maximo = input("Valor máximo: ")
        if minimo <= maximo:
            return minimo, maximo
        print("O mínimo não pode ser maior que o máximo.")

def filtrar_planetas():
    while True:
        print("\nSelecione uma opção: ")
        print("1 - Listar todos")
        print("2 - Filtrar por clima")
        print("3 - Filtrar por diâmetro")
        print("4 - Filtrar por gravidade")
        print("5 - Filtrar por população")
        print("0 - Voltar")
        opcao = input("Escolha: ")

        match opcao:
            case "0":
                return
            #case "1":
                #print(tabelaPlanetas)
            case "2":
                minimo, maximo = ler_intervalo()
                print("(a implementar)")
            case "3":
                minimo, maximo = ler_intervalo()
                print("(a implementar)")
            case "4":
                minimo, maximo = ler_intervalo()
                print("(a implementar)")
            case "5":
                minimo, maximo = ler_intervalo()
                print("(a implementar)")
            case _: #default
                print("Opção inválida, tente novamente.")

def filtrar_personagens():
    while True:
        print("\nSelecione uma opção: ")
        print("1 - Listar todos")
        print("2 - Filtrar por peso")
        print("3 - Filtrar por altura")
        print("4 - Filtrar por gênero")
        print("5 - Filtrar por cor do olho")
        print("0 - Voltar")
        opcao = input("Escolha: ")

        match opcao:
            case "0":
                return
            #case "1":
                #print(tabelaPersonagens)
            case "2":
                minimo, maximo = ler_intervalo()
                print("(a implementar)")
            case "3":
                minimo, maximo = ler_intervalo()
                print("(a implementar)")
            case "4":
                minimo, maximo = ler_intervalo()
                print("(a implementar)")
            case "5":
                print("Cor do olho:")
                print("1. Preto \n2.Castanho Escuro \n3.Blue \n4.Red \n5.Amarelo")
                print("6. Castanho Claro \n7.Rosa \n8.Laranja \n9.Dourado \n10.Branco")

        
            case _: #default
                print("Opção inválida, tente novamente.")

#FUNÇÕES E MENU************************************************************
while True: #menu de navegação
    print("________________________________________________")
    print("\nBem vindo ao sistema! O que gostaria de fazer?")
    print("1 - Pesquisar personagem")
    print("2 - Pesquisar planeta")
    print("3 - Filtrar Personagem")
    print("4 - Filtrar planetas")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            nomePersonagem = input("Digite o nome da(o) personagem que está buscando:\n")
            pesquisarPersonagem(nomePersonagem)
        case "2":
            nomePlaneta = input("Digite o nome do Planeta que está buscando:")
            pesquisarPlaneta(nomePlaneta)
        case "3":
            filtrar_personagens()
        case "4":
            filtrar_planetas()
        case "0":
            print("Programa encerrado com sucesso!")
            break
        case _:
            print("Opção inválida, tente novamente.")