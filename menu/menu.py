from consultas.filtros import filtrarPersonagens, filtrarPlanetas
from algoritmos.guloso import viagemEspacial

def exibir_informacoes(titulo, tabela):
    print(titulo)
    print("Fator de carga:", round(tabela.fator_de_carga() * 100, 2), "%")
    print("Número de colisões:", tabela.colisoes)

def menu(tabelaPlanetas, tabelaPersonagens):
        while True: #menu de navegação
            print( "________________________________________________\n" )
            print( "Bem vindo ao sistema! O que gostaria de fazer?" )
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
                    personagem = tabelaPersonagens.buscar(nomePersonagem)
                    if personagem is not None:
                        print(personagem)
                    else:
                        print("Personagem não encontrado.")
                case "2":
                    nomePlaneta = input( "Digite o nome do Planeta que está buscando:\n" )
                    planeta = tabelaPlanetas.buscar(nomePlaneta)
                    if planeta is not None:
                        print(planeta)
                    else:
                        print("Planeta não encontrado.")
                case "3":
                    filtrarPersonagens(tabelaPersonagens)
                  
                case "4":
                    filtrarPlanetas(tabelaPlanetas)
                case "5":
                    print( "Vamos ver quantas pessoas vamos poder levar nessa viagem!" )
                    planetaSaida = input( "Digite de qual planeta a viagem vai partir:\n" )
                    planetaDestino = input( "Qual planeta é o destino desta viagem?\n" )
                    capacidadeNave = int( input( "Qual a capacidade da sua nave?(kg)\n" ) )
                    viagemEspacial( tabelaPersonagens,  planetaSaida, planetaDestino, capacidadeNave )
                case "0":
                    print( "Programa encerrado com sucesso!" )
                    return