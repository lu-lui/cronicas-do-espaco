from consultas.filtros import filtrarPersonagens, filtrarPlanetas
from algoritmos.guloso import viagemEspacial

def menu(gerenciadorPlanetas, gerenciadorPersonagens):
        while True: #menu de navegação
            print( "________________________________________________\n" )
            print( "Bem vindo ao sistema! O que gostaria de fazer?" )
            print( "1 - Pesquisar personagem (nome exato)" )
            print( "2 - Pesquisar planeta (nome exato)" )
            print( "3 - Pesquisar personagem (prefixo)" )
            print( "4 - Pesquisar planeta (prefixo)" )
            print( "5 - Filtrar personagens" )
            print( "6 - Filtrar planetas" )
            print( "7 - Planejar viagem espacial" )
            print( "0 - Sair" )
            opcao = input( "Escolha uma opção: " )

            while opcao != "0" and opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4" and opcao != "5" and opcao != "6" and opcao != "7":
                opcao = input( "Opção inválida! Tente novamente:" )

            match opcao:
                case "1":
                    nomePersonagem = input( "Digite o nome da(o) personagem que está buscando:\n" )
                    personagem = gerenciadorPersonagens.buscar_nome(nomePersonagem)
                    if personagem is not None:
                        print(personagem)
                    else:
                        print("Personagem não encontrado.")

                case "2":
                    nomePlaneta = input( "Digite o nome do Planeta que está buscando:\n" )
                    planeta = gerenciadorPlanetas.buscar_nome(nomePlaneta)
                    if planeta is not None:
                        print(planeta)
                    else:
                        print("Planeta não encontrado.")

                case "3":
                    prefixoPersonagem = input( "Digite o prefixo que está buscando:\n" )
                    resultadosPersonagens = gerenciadorPersonagens.buscar_prefixo(prefixoPersonagem)
                    personagem = selecionarResultado(resultadosPersonagens)
                    if personagem is not None:
                        print(personagem)

                case "4":
                    prefixoPlaneta = input( "Digite o nome do Planeta que está buscando:\n" )
                    resultadosPlanetas = gerenciadorPlanetas.buscar_prefixo(prefixoPlaneta)
                    planeta = selecionarResultado(resultadosPlanetas)
                    if planeta is not None:
                        print(planeta)

                case "5":
                    filtrarPersonagens(gerenciadorPersonagens)
                  
                case "6":
                    filtrarPlanetas(gerenciadorPlanetas)

                case "7":
                    print( "Vamos ver quantas pessoas vamos poder levar nessa viagem!" )
                    planetaSaida = input( "Digite de qual planeta a viagem vai partir:\n" )
                    planetaDestino = input( "Qual planeta é o destino desta viagem?\n" )
                    capacidadeNave = ler_valor( "Qual a capacidade da sua nave?(kg)\n" )
                    viagemEspacial( gerenciadorPersonagens,  planetaSaida, planetaDestino, capacidadeNave )
                
                case "0":
                    print( "Programa encerrado com sucesso!" )
                    return

def selecionarResultado(resultados):
    if not resultados:
        print("Nenhum resultado encontrado.\n")
        return
    else:
        i = 1
        print("0 . Voltar")
        for elemento in resultados:
            print(i, ".", elemento.name)
            i += 1

        indice = ler_valor("\nQual resultado deseja imprimir? ") - 1

        if indice == -1:
            return
        
        while indice < 0 or indice >= len(resultados):
            indice = ler_valor( "\nOpção inválida! Tente novamente:" ) - 1

        return resultados[indice]

def ler_valor(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
        except ValueError:
            print( "Digite apenas números" )
            continue
        return valor