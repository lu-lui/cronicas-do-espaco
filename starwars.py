import requests #se der erro colocar no terminal "pip install requests"

#PLANETAS ****************************************************************
#-------------------------------FUNÇÕES-----------------------------------
def funcao_hash_planetas( chave ):      #função pra mapear os id's (chave) pra hash
    soma = 0

    for caractere in chave:
        soma += ord( caractere )        #ord transforma letra em número
    return soma % tamanhoPlanetas       #posição na tabela hash

def inserir_planeta( planeta ):
    chave = planeta[ "name" ]
    posicao = funcao_hash_planetas( chave )

    #depois de achar a posição se houver colisão vamos fazer a sondagem quadrática
    i = 0
    colisoes = 0
    #fórmula da sondagem quadrática (h + i^2) % tamanho (nesse caso 89)
    #h nossa posição inicialmente calculada e i o número de tentativas 
    #que fizemos de achar um lugar vazio
    while tabelaPlanetas[ ( posicao + i**2 ) % tamanhoPlanetas ] is not None: 
        colisoes += 1
        i += 1

    #dicionário só com os dados que a gnt quer de cada corpo - parsing
    novo_planeta = {
        "name": planeta[ "name" ],
        "climate": planeta[ "climate" ],
        "diameter": planeta[ "diameter" ],
        "gravity": planeta[ "gravity" ],
        "population": planeta[ "population" ],
    }

    nova_posicao = ( posicao + i**2 ) % tamanhoPlanetas   #a nova posição é a que fez o loop parar
    tabelaPlanetas[ nova_posicao ] = novo_planeta

    return colisoes

#-------------------------------CHAMADA API-----------------------------------
#fator carga -> 60 planetas e no máximo 70% ocupação
# -> 60/m = 0,7 -> m = 85 -> hash com 89 posições

tamanhoPlanetas = 89
tabelaPlanetas = [ None ] * tamanhoPlanetas
numColisoesPlanetas = 0

planetasLink = "http://swapi.dev/api/planets/"

while planetasLink is not None:
    planetasRespostas = requests.get( planetasLink )
    planetasDados = planetasRespostas.json()

    for planeta in planetasDados[ "results" ]:
        numColisoesPlanetas += inserir_planeta( planeta )

    planetasLink = planetasDados[ "next" ]
#-------------------------------MAIN PLANETAS-----------------------------------
qtdElementosPlanetas = 0

#contando elementos inseridos pra calcular o fator de carga
for posicao in tabelaPlanetas:
    if posicao is not None:
        qtdElementosPlanetas += 1

fatorCargaPlanetas = qtdElementosPlanetas / tamanhoPlanetas
print( "Planetas__________________________________" )
print( "Fator de carga:", round( fatorCargaPlanetas * 100, 2 ), "%" ) #arredondamos p 2 casas
print( "Número de colisões no carregamento:", numColisoesPlanetas )

#Personagem ****************************************************************
#-------------------------------FUNÇÕES-----------------------------------
def funcao_hash_personagens( chave ):       #função pra mapear os id's (chave) pra hash
    soma = 0

    for caractere in chave:
        soma += ord( caractere )            #ord transforma letra em número
    return soma % tamanhoPersonagens        #posição na tabela hash

def inserir_personagem( personagem ):
    chave = personagem[ "name" ]
    posicao = funcao_hash_personagens( chave )

    #depois de achar a posição se houver colisão vamos fazer a sondagem quadrática
    i = 0
    colisoes = 0
    #fórmula da sondagem quadrática (h + i^2) % tamanho (nesse caso 127)
    #h nossa posição inicialmente calculada e i o número de tentativas 
    #que fizemos de achar um lugar vazio
    while tabelaPersonagens[ ( posicao + i**2 ) % tamanhoPersonagens ] is not None: 
        colisoes += 1
        i += 1

    linkHomeworld = personagem[ "homeworld" ]
    respostaHomeWorld = requests.get( linkHomeworld )
    dadosHomeworld = respostaHomeWorld.json()
    nomeHomeWorld = dadosHomeworld[ "name" ]

    #dicionário só com os dados que a gnt quer de cada corpo - parsing
    nova_personagem = {
        "name": personagem[ "name" ],
        "mass": personagem[ "mass" ],
        "height": personagem[ "height" ],
        "gender": personagem[ "gender" ],
        "eye_color": personagem[ "eye_color" ],
        "homeworld": nomeHomeWorld
    }

    nova_posicao = ( posicao + i**2 ) % tamanhoPersonagens   #a nova posição é a que fez o loop parar
    tabelaPersonagens[ nova_posicao ] = nova_personagem

    return colisoes

#-------------------------------CHAMADA API-----------------------------------
#fator carga -> 82 personagens e no máximo 70% ocupação
# -> 82/m = 0,7 -> m = 117 -> hash com 127 posições

tamanhoPersonagens = 127
tabelaPersonagens = [ None ] * tamanhoPersonagens
numColisoesPersonagem = 0

PersonagemLink = "http://swapi.dev/api/people/"

while PersonagemLink is not None:
    PersonagemRespostas = requests.get( PersonagemLink )
    PersonagemDados = PersonagemRespostas.json()

    for personagem in PersonagemDados[ "results" ]:
        numColisoesPersonagem += inserir_personagem( personagem )

    PersonagemLink = PersonagemDados[ "next" ]
#-------------------------------MAIN PERSONAGENS-----------------------------------
qtdElementosPersonagem = 0

#contando elementos inseridos pra calcular o fator de carga
for posicao in tabelaPersonagens:
    if posicao is not None:
        qtdElementosPersonagem += 1

fatorCargaPersonagem = qtdElementosPersonagem / tamanhoPersonagens
print( "Personagens_____________________________" )
print( "Fator de carga:", round( fatorCargaPersonagem * 100, 2 ), "%" ) #arredondamos p 2 casas
print( "Número de colisões no carregamento:", numColisoesPersonagem )

#--------------------------Pesquisa e Listagem-----------------------------
def buscaPlanetas( chave ): 
    soma = 0
    i = 0

    for caractere in chave:
        soma += ord( caractere )  
    posicaoInicial = soma % tamanhoPlanetas
    posicao = posicaoInicial

    while tabelaPlanetas[ posicao ] != None and tabelaPlanetas[ posicao ][ "name" ] != chave and i < tamanhoPlanetas:
        i += 1
        posicao = ( posicaoInicial + i**2 ) % tamanhoPlanetas 

    if i == tamanhoPlanetas or tabelaPlanetas[ posicao ] == None:
        print( "Planeta não encontrado." )
        return
    else:
        planeta = tabelaPlanetas[ posicao ]
        print( "Name: ", planeta[ "name" ] )
        print( "Climate: ", planeta[ "climate" ] )
        print( "Diameter: ", planeta[ "diameter" ] )
        print( "Gravity: ", planeta[ "gravity" ] )
        print( "Population: ", planeta[ "population" ] )
        return

def buscaPersonagens( chave ): 
    soma = 0
    i = 0

    for caractere in chave:
        soma += ord( caractere )  
    posicaoInicial = soma % tamanhoPersonagens
    posicao = posicaoInicial

    while tabelaPersonagens[ posicao ] != None and tabelaPersonagens[ posicao ][ "name" ] != chave and i < tamanhoPersonagens:
        i += 1
        posicao = ( posicaoInicial + i**2 ) % tamanhoPersonagens 

    if i == tamanhoPersonagens or tabelaPersonagens[ posicao ] == None:
        print( "Personagem não encontrado." )
        return
    else:
        personagem = tabelaPersonagens[ posicao ]
        print( "Name: ", personagem[ "name" ] )
        print( "Mass: ", personagem[ "mass" ] )
        print( "Height: ", personagem[ "height" ] )
        print( "Gender: ", personagem[ "gender" ] )
        print( "Eye color: ", personagem[ "eye_color" ] )
        print( "Homeworld: ", personagem[ "homeworld" ] )
        return

def ler_intervalo():
    while True:
        try:
            minimo = int( input( "Valor mínimo: " ) )
            maximo = int( input( "Valor máximo: " ) )
        except ValueError:
            print( "Digite apenas numeros inteiros" )
            continue
        
        if minimo <= maximo:
            return minimo, maximo
        print( "O mínimo não pode ser maior que o máximo." )

def filtrarPlanetas():
    while True:
        print( "\nSelecione uma opção: " )
        print( "1 - Listar todos" )
        print( "2 - Filtrar por clima" )
        print( "3 - Filtrar por diâmetro" )
        print( "4 - Filtrar por gravidade" )
        print( "5 - Filtrar por população" )
        print( "0 - Voltar" )
        opcao = input( "Escolha: " )
                
        while opcao != "0" and opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4" and opcao != "5":
            opcao = input( "Opção inválida! Tente novamente:" )

        match opcao:
            case "0":
                return
            case "1":
                flag = False
                for planeta in tabelaPlanetas:
                    if planeta is not None:
                        print( "\nName: ", planeta[ "name" ] )
                        print( "Climate: ", planeta[ "climate" ] )
                        print( "Diameter: ", planeta[ "diameter" ] )
                        print( "Gravity: ", planeta[ "gravity" ] )
                        print( "Population: ", planeta[ "population" ] )
                        flag = True
                if not flag:                      
                    print( "Nenhum resultado encontrado." )
            case "2":
                print( "\n---Clima---" )
                print( "Selecione o clima desejado:" )
                opcao = input( "1. Temperado \n2. Arido \n3. Tropical \n4. Quente \n5. Outros\n" )

                while opcao not in [ "1", "2", "3", "4", "5" ]:
                    print( "Opção inválida! \nSelecione um clima:" )
                    opcao = input( "1. Temperado \n2. Arido \n3. Tropical \n4. Quente \n5. Outros\n" )

                flag = False #flag que liga quando acha a informação  
                match opcao:
                    case "1":
                        for planeta in tabelaPlanetas: #os planetas tem mais de uma caracteristica climática
                            if planeta is not None:    #verifica se a temperatura selecionada está etre elas
                                if "temperate" in planeta[ "climate" ]: 
                                    print( "\nName: ", planeta[ "name" ] )
                                    print( "Climate: ", planeta[ "climate" ] )
                                    flag = True
                    case "2":
                        for planeta in tabelaPlanetas:
                            if planeta is not None:
                                if "arid" in planeta[ "climate" ]:
                                    print( "\nName: ", planeta[ "name" ] )
                                    print( "Climate: ", planeta[ "climate" ] )
                                    flag = True            
                    case "3":
                        for planeta in tabelaPlanetas:
                            if planeta is not None:
                                if "tropical" in planeta[ "climate" ]:
                                    print( "\nName: ", planeta[ "name" ] )
                                    print( "Climate: ", planeta[ "climate" ] )
                                    flag = True
                    case "4":
                        for planeta in tabelaPlanetas:
                            if planeta is not None:
                                if "hot" in planeta[ "climate" ]:
                                    print( "\nName: ", planeta[ "name" ] )
                                    print( "Climate: ", planeta[ "climate" ] )
                                    flag = True
                    case "5":
                        for planeta in tabelaPlanetas:
                            if planeta is not None:
                                if "temperate" not in planeta[ "climate" ] and "arid" not in planeta[ "climate" ] and "tropical" not in planeta[ "climate" ] and "hot" not in planeta[ "climate" ]:
                                    print( "\nName: ", planeta[ "name" ] )
                                    print( "Climate: ", planeta[ "climate" ] )
                                    flag = True
                if not flag:                      
                    print( "Nenhum resultado encontrado." )
            case "3":
                print( "\n---Diâmetro---" )
                print( "Digite o intervalo de diâmetro:" )
                minimo, maximo = ler_intervalo()

                flag = False
                for planeta in tabelaPlanetas:
                    if planeta is not None:
                        if planeta[ "diameter" ] != "unknown":
                            if minimo <= int( planeta[ "diameter" ] ) <= maximo:
                                print( "\nName: ", planeta[ "name" ] )
                                print( "Diameter: ", planeta[ "diameter" ] )
                                flag = True
                if not flag:                      
                    print( "Nenhum resultado encontrado." )
                        
            case "4":
                print( "\n---Gravidade---" )
                gravidade = input( "Digite a gravidade exata (ex: 1 standard): " )

                flag = False
                for planeta in tabelaPlanetas:
                    if planeta is not None:
                        if planeta[ "gravity" ] == gravidade:
                            print( "\nName: ", planeta[ "name" ] )
                            print( "Gravity: ", planeta[ "gravity" ] )
                            flag = True
                if not flag:                      
                    print( "Nenhum resultado encontrado." )
            case "5":
                print( "\n---População---" )
                print( "Digite o intervalo de população:" )
                minimo, maximo = ler_intervalo()

                flag = False
                for planeta in tabelaPlanetas:
                    if planeta is not None:
                        if planeta[ "population" ] != "unknown":
                            if minimo <= int( planeta[ "population" ] ) <= maximo:
                                print( "\nName: ", planeta[ "name" ] )
                                print( "Population: ", planeta[ "population" ] )
                                flag = True
                if not flag:                      
                    print( "Nenhum resultado encontrado." )          

def filtrarPersonagens():
    while True:
        print( "\nSelecione uma opção: " )
        print( "1 - Listar todos" )
        print( "2 - Filtrar por peso" )
        print( "3 - Filtrar por altura" )
        print( "4 - Filtrar por gênero" )
        print( "5 - Filtrar por cor dos olhos" )
        print( "6 - Filtrar por planeta" )
        print( "0 - Voltar" )
        opcao = input( "Escolha: " )
        
        while opcao != "0" and opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4" and opcao != "5" and opcao != "6":
            opcao = input( "Opção inválida! Tente novamente:" )

        match opcao:
            case "0":
                return
            case "1":
                flag = False
                for personagem in tabelaPersonagens:
                    if personagem is not None:
                        print( "\nName: ", personagem[ "name" ] )
                        print( "Mass: ", personagem[ "mass" ] )
                        print( "Height: ", personagem[ "height" ] )
                        print( "Gender: ", personagem[ "gender" ] )
                        print( "Eye Color: ", personagem[ "eye_color" ] )
                        flag = True
                if not flag:                      
                    print( "Nenhum resultado encontrado." )
            case "2":
                print( "\n---Peso---" )
                print( "Digite o intervalo de peso:" )
                minimo, maximo = ler_intervalo()

                flag = False
                for personagem in tabelaPersonagens:
                    if personagem is not None:
                        if personagem[ "mass" ] != "unknown":
                            if minimo <= float( personagem[ "mass" ].replace( "," , "" ) ) <= maximo:
                                print( "\nName: ", personagem[ "name" ] )
                                print( "Mass: ", personagem[ "mass" ] ) 
                                flag = True
                if not flag:                      
                    print( "Nenhum resultado encontrado." )                  
            case "3":
                print( "\n---Altura---" )
                print( "Digite o intervalo de altura:" )
                minimo, maximo = ler_intervalo()

                flag = False
                for personagem in tabelaPersonagens:
                    if personagem is not None:
                        if personagem[ "height" ] != "unknown":
                            if minimo <= int( personagem[ "height" ] ) <= maximo:
                                print( "\nName: ", personagem[ "name" ] )
                                print( "Height: ", personagem[ "height" ] ) 
                                flag = True
                if not flag:                      
                    print( "Nenhum resultado encontrado." )              
            case "4":
                print( "\n---Gênero---" )
                print( "Selecione o gênero:" )
                opcao = input( "1. Feminino \n2. Masculino\n" )

                while opcao != "1" and opcao != "2":
                    print( "Opção inválida! \nSelecione um gênero:" )
                    opcao = input( "1. Feminino \n2. Masculino\n" )   
                
                if opcao == "1":
                    flag = False
                    for personagem in tabelaPersonagens:
                        if personagem is not None:
                            if( personagem[ "gender" ] == "female" ):
                                print( "\nName: ", personagem[ "name" ] )
                                print( "Gender: ", personagem[ "gender" ] )
                                flag = True
                    if not flag:                      
                        print( "Nenhum resultado encontrado." )
                elif opcao == "2":
                    flag = False
                    for personagem in tabelaPersonagens:
                        if personagem is not None:
                            if( personagem[ "gender" ] == "male" ):
                                print( "\nName: ", personagem[ "name" ] )
                                print( "Gender: ", personagem[ "gender" ] )
                                flag = True
                    if not flag:                      
                        print( "Nenhum resultado encontrado." ) 
            case "5":
                print( "\n---Cor dos olhos---" )
                print( "Selecione a cor desejada:" )
                opcao = input( "1. Preto \n2. Castanho \n3. Azul \n4. Amarelo \n5. Colorido\n" )

                while opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4" and opcao != "5":
                    print( "Opção inválida! \nSelecione uma cor de olhos:" )
                    opcao = input( "1. Preto \n2. Castanho \n3. Azul \n4. Amarelo \n5. Colorido\n" )

                flag = False  
                match opcao:
                    case "1":
                        for personagem in tabelaPersonagens:
                            if personagem is not None:
                                if( personagem[ "eye_color" ] == "black" ):
                                    print( "\nName: ", personagem[ "name" ] )
                                    print( "Eye Color: ", personagem[ "eye_color" ] )
                                    flag = True
                    case "2":
                        for personagem in tabelaPersonagens:
                            if personagem is not None:
                                if( personagem[ "eye_color" ] == "brown" or personagem[ "eye_color" ] == "hazel" ):
                                    print( "\nName: ", personagem[ "name" ] )
                                    print( "Eye Color: ", personagem[ "eye_color" ] )
                                    flag = True
                    case "3":
                        for personagem in tabelaPersonagens:
                            if personagem is not None:
                                if( personagem[ "eye_color" ] == "blue" ):
                                    print( "\nName: ", personagem[ "name" ] )
                                    print( "Eye Color: ", personagem[ "eye_color" ] )
                                    flag = True
                    case "4":
                        for personagem in tabelaPersonagens:
                            if personagem is not None:
                                if( personagem[ "eye_color" ] == "yellow" ):
                                    print( "\nName: ", personagem[ "name" ] )
                                    print( "Eye Color: ", personagem[ "eye_color" ] )
                                    flag = True
                    case "5":
                        for personagem in tabelaPersonagens:
                            if personagem is not None:
                                if personagem[ "eye_color" ] not in [ "black", "brown", "hazel", "blue", "yellow", "" ]:
                                    print( "\nName: ", personagem[ "name" ] )
                                    print( "Eye Color: ", personagem[ "eye_color" ] )
                                    flag = True
                if not flag:                      
                    print( "Nenhum resultado encontrado." )
            case "6":
                flag = False
                p = input( "Digite o planeta: \n" )
                for personagem in tabelaPersonagens:
                    if personagem is not None:
                        if( personagem[ "homeworld" ] == p ):
                            print( "\nName: ", personagem[ "name" ] )
                            print( "Homeworld: ", personagem[ "homeworld" ] )
                            print( "Massa: ", personagem[ "mass" ] )
                            flag = True
                if not flag:                      
                    print( "Nenhum resultado encontrado." ) 

#ALGORITMO GULOSO**********************************************************
#QUAL O MÁXIMO DE PESSOAS QUE CONSEGUIMOS LEVAR DO PLANETA X AO Y EM UMA NAVE 
#COM DETERMINADA CAPACIDADE
def viagemEspacial( planetaSaida, planetaDestino, capacidade ):
    pessoasPossiveis = []

    for personagem in tabelaPersonagens:
        if personagem is not None and personagem[ "mass" ] != "unknown":
            if personagem[ "homeworld" ] == planetaSaida:
                pessoasPossiveis.append( personagem )

    pessoasPossiveisOrdenadas = sorted( pessoasPossiveis, key=lambda p: float( p[ "mass" ] ) )

    cargaNave = 0
    tamVetor = len( pessoasPossiveisOrdenadas )
    pessoasQueVao = []
    i = 0
    contPessoas = 0

    while i < tamVetor:
        peso = float( pessoasPossiveisOrdenadas[ i ][ "mass" ] )
        if cargaNave + peso <= capacidade:
            pessoasQueVao.append( pessoasPossiveisOrdenadas[ i ] )
            cargaNave += peso
            contPessoas += 1
            i += 1
        else:
            break

    print( f"Vamos levar { contPessoas } pessoas de { planetaSaida } para { planetaDestino }!" )
    print( "Lista de passageiros:" )
    i = 0
    for personagem in pessoasQueVao:
        i += 1
        print( i, ":", personagem[ "name" ] )

    return

#FUNÇÕES E MENU************************************************************
while True: #menu de navegação
    print( "________________________________________________" )
    print( "\nBem vindo ao sistema! O que gostaria de fazer?" )
    print( "1 - Pesquisar personagem" )
    print( "2 - Pesquisar planeta" )
    print( "3 - Filtrar personagens" )
    print( "4 - Filtrar planetas" )
    print( "5 - Planejar viagem espacial" )
    print( "0 - Sair" )
    opcao = input( "Escolha uma opção: " )

    while opcao != "0" and opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4" and opcao != "5":
        opcao = input( "Opção inválida! Tente novamente:" )

    match opcao:
        case "1":
            nomePersonagem = input( "Digite o nome da(o) personagem que está buscando:\n" )
            buscaPersonagens( nomePersonagem )
        case "2":
            nomePlaneta = input( "Digite o nome do Planeta que está buscando:\n" )
            buscaPlanetas( nomePlaneta )
        case "3":
            filtrarPersonagens()
        case "4":
            filtrarPlanetas()
        case "5":
            print( "Vamos ver quantas pessoas vamos poder levar nessa viagem!" )
            planetaSaida = input( "Digite de qual planeta a viagem vai partir:\n" )
            planetaDestino = input( "Qual planeta é o destino desta viagem?\n" )
            capacidadeNave = int( input( "Qual a capacidade da sua nave?(kg)\n" ) )
            viagemEspacial( planetaSaida, planetaDestino, capacidadeNave )
        case "0":
            print( "Programa encerrado com sucesso!" )
            break