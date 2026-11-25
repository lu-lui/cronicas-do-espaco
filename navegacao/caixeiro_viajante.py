from .grafos import Grafos
from .funcoes_principais import alterar_rotulo, limpar_terminal, ler_valor, mostrarPlanetas, exibir

planetas_missao = ["Alderaan", "Cerea", "Chandrila", "Corellia", "Coruscant", "Kashyyyk", "Malastare", "Naboo", "Shili", "Umbara"]

def criar_grafo(gerenciadorPlanetas, nomes):
    grafo = Grafos()
    for nome in nomes:
        planeta = gerenciadorPlanetas.buscar_nome(nome)
        grafo.add_vertice(planeta)

    #criação do grafo, com pesos inventados para implementação do caixeiro viajante
    grafo.add_aresta("Alderaan", "Cerea", 8)
    grafo.add_aresta("Alderaan", "Chandrila", 2)
    grafo.add_aresta("Alderaan", "Corellia", 2)
    grafo.add_aresta("Alderaan", "Coruscant", 3)
    grafo.add_aresta("Alderaan", "Kashyyyk", 9)
    grafo.add_aresta("Alderaan", "Naboo", 9)
    grafo.add_aresta("Cerea", "Coruscant", 7)
    grafo.add_aresta("Cerea", "Malastare", 9)
    grafo.add_aresta("Cerea", "Naboo", 10)
    grafo.add_aresta("Cerea", "Umbara", 12)
    grafo.add_aresta("Chandrila", "Coruscant", 1)
    grafo.add_aresta("Corellia", "Umbara", 8)
    grafo.add_aresta("Coruscant", "Shili", 5)
    grafo.add_aresta("Kashyyyk", "Naboo", 9)
    grafo.add_aresta("Kashyyyk", "Shili", 9)
    grafo.add_aresta("Kashyyyk", "Umbara", 2)
    grafo.add_aresta("Malastare", "Naboo", 2)
    grafo.add_aresta("Naboo", "Shili", 11)
    return grafo

def roteiro_missao(grafo, origem, destinos):
    melhor = { "custo": float("inf"), "rota": None }

    def explorar(atual, caminho, custo):
        if custo >= melhor["custo"]:
            return

        passou_todos = True
        for destino in destinos:
            if destino not in caminho:
                passou_todos = False

        if passou_todos and origem in grafo.adjacencia[atual]:
            total = custo + grafo.adjacencia[atual][origem]
            if total < melhor["custo"]:
                melhor["custo"] = total
                melhor["rota"] = caminho + [origem]

        for vizinho in grafo.adjacencia[atual]:
            if vizinho not in caminho:
                peso = grafo.adjacencia[atual][vizinho]
                caminho.append(vizinho)
                explorar(vizinho, caminho, custo + peso)
                caminho.pop()

    explorar(origem, [origem], 0)
    if melhor["rota"] is None:
        return None, None
    return melhor["rota"], melhor["custo"]   

def planejarMissao_1(gerenciadorPlanetas, entrada, resultado, rotulo, definir_acao, label_capa, label_grafoPlanetas, label_grafoPersonagens ):
    limpar_terminal(label_grafoPersonagens, label_grafoPlanetas, label_capa, resultado)
    resultado.pack_forget()
    label_grafoPlanetas.pack(anchor="n")
    resultado.pack(side = "left", fill="both", expand=True)
    grafo = criar_grafo(gerenciadorPlanetas, planetas_missao)
    mostrarPlanetas(resultado)
    resultado.insert("end", "Vamos realizar uma viagem saindo da base, passando por vários destinos e retornando a base!\n")
    alterar_rotulo("Escolha o planeta de origem: ", rotulo)
    definir_acao(lambda:planejarMissao_2(grafo, gerenciadorPlanetas, entrada, resultado, rotulo, definir_acao, label_grafoPlanetas ))

def planejarMissao_2(grafo, gerenciadorPlanetas, entrada, resultado, rotulo, definir_acao, label_grafoPlanetas ):
    numero = ler_valor(entrada, rotulo)
    entrada.delete(0, "end")

    if numero is None:
        return

    if numero < 1 or numero > len(planetas_missao):
        resultado.delete("1.0", "end")
        resultado.insert("end", "Opção inválida! Tente novamente: ")
        return

    origem = planetas_missao[numero - 1]
    destinos = []

    alterar_rotulo("Escolha um destino (0 para terminar): ", rotulo)

    definir_acao(lambda: planejarMissao_3(
        origem, grafo, gerenciadorPlanetas, entrada,
        resultado, rotulo, definir_acao, destinos, label_grafoPlanetas 
    ))


def planejarMissao_3(origem, grafo, gerenciadorPlanetas, entrada, resultado, rotulo, definir_acao, destinos, label_grafoPlanetas ):
    numero = ler_valor(entrada, rotulo)
    entrada.delete(0, "end")

    if numero is None:
        return

    if numero == 0:
        if len(destinos) == 0:
            resultado.delete("1.0", "end")
            resultado.insert("end", "Erro! Nenhum destino foi escolhido")
            return

        rota, custo = roteiro_missao(grafo, origem, destinos)

        resultado.delete("1.0", "end")

        if rota is None:
            resultado.insert("end", "Não existe roteiro que passe por esses planetas sem repetir nenhum.")
        else:
            resultado.insert("end", exibir(grafo, rota, custo, destinos))

        return

    if numero < 1 or numero > len(planetas_missao):
        alterar_rotulo("Opção inválida! Tente novamente: ", rotulo)
    else:
        destinos.append(planetas_missao[numero - 1])

    alterar_rotulo("Escolha mais um destino (0 para terminar): ", rotulo)

    definir_acao(lambda: planejarMissao_3(
        origem, grafo, gerenciadorPlanetas, entrada,
        resultado, rotulo, definir_acao, destinos, label_grafoPlanetas 
    ))
