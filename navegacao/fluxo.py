from .grafos import Grafos
from .funcoes_principais import alterar_rotulo, limpar_terminal, ler_valor, mostrarPersonagens

personagens = [ "C-3PO", "Chewbacca", "Han Solo", "Leia Organa", "Luke Skywalker", 
               "Obi-Wan Kenobi", "R2-D2", "Yoda" ]

def criar_grafo( gerenciadorPersonagens, nomes  ):
    grafo = Grafos()
    for nome in nomes:
        personagem = gerenciadorPersonagens.buscar_nome( nome )
        grafo.add_vertice( personagem )

    #criação do grafo, com pesos inventados para implementação do caixeiro viajante
    grafo.add_aresta( "Luke Skywalker", "R2-D2", 10 )
    grafo.add_aresta( "Luke Skywalker", "Obi-Wan Kenobi", 20 )
    grafo.add_aresta( "Luke Skywalker", "Han Solo", 10 )
    grafo.add_aresta( "R2-D2", "Luke Skywalker", 10 )
    grafo.add_aresta( "R2-D2", 'Obi-Wan Kenobi', 5 )
    grafo.add_aresta( "R2-D2", "C-3PO", 1 )
    grafo.add_aresta( "R2-D2", "Yoda", 6 )
    grafo.add_aresta( "Obi-Wan Kenobi", "Luke Skywalker", 20 )
    grafo.add_aresta( "Obi-Wan Kenobi", "R2-D2", 5 )
    grafo.add_aresta( "Obi-Wan Kenobi", "Han Solo", 3 )
    grafo.add_aresta( "Obi-Wan Kenobi", "Chewbacca", 5 )
    grafo.add_aresta( "Obi-Wan Kenobi", "Yoda", 7 )
    grafo.add_aresta( "Obi-Wan Kenobi", "C-3PO", 6 )
    grafo.add_aresta( "Han Solo", "Luke Skywalker", 10 )
    grafo.add_aresta( "Han Solo", "Obi-Wan Kenobi", 3 )
    grafo.add_aresta( "Han Solo", "Yoda", 4 )
    grafo.add_aresta( "Han Solo", "Chewbacca", 8 )
    grafo.add_aresta( "C-3PO", "R2-D2", 1 )
    grafo.add_aresta( "C-3PO", "Yoda", 3 )
    grafo.add_aresta( "C-3PO", "Obi-Wan Kenobi", 6 )
    grafo.add_aresta( "C-3PO", "Leia Organa", 20 )
    grafo.add_aresta( "Yoda", "Obi-Wan Kenobi", 7 )
    grafo.add_aresta( "Yoda", "Han Solo", 4 )
    grafo.add_aresta( "Yoda", "Chewbacca", 2 )
    grafo.add_aresta( "Yoda", "C-3PO", 6 )
    grafo.add_aresta( "Yoda", "R2-D2", 6 )
    grafo.add_aresta( "Yoda", "Leia Organa", 10 )
    grafo.add_aresta( "Chewbacca", "Han Solo", 8 )
    grafo.add_aresta( "Chewbacca", "Yoda", 2 )
    grafo.add_aresta( "Chewbacca", "Obi-Wan Kenobi", 5 )
    grafo.add_aresta( "Chewbacca", "Leia Organa", 10 )
    grafo.add_aresta( "Leia Organa", "Chewbacca", 10 )
    grafo.add_aresta( "Leia Organa", "Yoda", 10 )
    grafo.add_aresta( "Leia Organa", "C-3PO",20 )
    return grafo

def buscar_caminho( capacidade_restante, atual, destino, visitados, caminho ):
    visitados.append( atual )
    caminho.append( atual )

    if atual == destino:
        return True

    for vizinho in capacidade_restante[ atual ]:

        if vizinho not in visitados and capacidade_restante[ atual ][ vizinho ] > 0:
            encontrou = buscar_caminho( capacidade_restante, vizinho, destino, visitados, caminho )

            if encontrou:
                return True

    caminho.pop()
    return False

def ford_fulkerson( resultado, grafo, origem, destino ):
    capacidade_restante = {}

    for vertice in grafo.adjacencia:
        capacidade_restante[ vertice ] = {}

        for vizinho in grafo.adjacencia[ vertice ]:
            capacidade_restante[ vertice ][ vizinho ] = grafo.adjacencia[ vertice ][ vizinho ]

    fluxo_maximo = 0

    while True:
        visitados = []
        caminho = []
        encontrou = buscar_caminho( capacidade_restante, origem, destino, visitados, caminho )

        if not encontrou:
            break

        capacidade_caminho = float( "inf" )
        atual = caminho[ 0 ]

        for proximo in caminho[ 1: ]:
            capacidade = capacidade_restante[ atual ][ proximo ]

            if capacidade < capacidade_caminho:
                capacidade_caminho = capacidade

            atual = proximo

        atual = caminho[ 0 ]

        for proximo in caminho[ 1: ]:
            capacidade_restante[ atual ][ proximo ] -= capacidade_caminho

            if atual not in capacidade_restante[ proximo ]:
                capacidade_restante[ proximo ][ atual ] = 0

            capacidade_restante[ proximo ][ atual ] += capacidade_caminho

            atual = proximo

        fluxo_maximo += capacidade_caminho

        resultado.insert( "end", f"Caminho encontrado: { ' -> '.join( caminho ) }" )
        resultado.insert( "end", f"Fluxo enviado: { capacidade_caminho }" )

    return fluxo_maximo

def entregarMensagem1( gerenciadorPersonagens, entrada, resultado, rotulo, definir_acao, 
                      label_capa, label_grafoPlanetas, label_grafoPersonagens ):
    
    limpar_terminal( label_grafoPersonagens, label_grafoPlanetas, label_capa, resultado )
    grafo = criar_grafo( gerenciadorPersonagens, personagens )
    resultado.pack_forget()
    label_grafoPersonagens.pack( anchor = "n" )
    resultado.pack( side = "left", fill = "both", expand = True )

    resultado.delete( "1.0", "end" )
    resultado.insert( "end", "Vamos enviar mensagens de um personagem ao outro! Selecione o remetente e o destino e quantas mensagens gostaria de enviar e vamos ver se temos capacidade de fluxo para entregar as mensagens!\n" )
    mostrarPersonagens( resultado )

    alterar_rotulo( "Escolha o remetente da mensagem: ", rotulo )
    definir_acao( lambda : entregarMensagem2( grafo, gerenciadorPersonagens, entrada, resultado, rotulo, definir_acao, 
                label_capa, label_grafoPlanetas, label_grafoPersonagens ) )

def entregarMensagem2( grafo, gerenciadorPersonagens, entrada, resultado, rotulo, definir_acao, 
                      label_capa, label_grafoPlanetas, label_grafoPersonagens ):
    numero = ler_valor( entrada, rotulo )
    entrada.delete( 0, "end" )

    if numero is None:
        alterar_rotulo( "Opção inválida! Tente novamente:", rotulo )
        definir_acao( lambda : entregarMensagem2( grafo, gerenciadorPersonagens, entrada, resultado, 
                    rotulo, definir_acao, label_capa, label_grafoPlanetas, label_grafoPersonagens ) )
        return

    if numero < 1 or numero > len( personagens ):
        alterar_rotulo( "Opção inválida! Tente novamente:", rotulo )
        definir_acao( lambda : entregarMensagem2( grafo, gerenciadorPersonagens, entrada, resultado, 
                    rotulo, definir_acao, label_capa, label_grafoPlanetas, label_grafoPersonagens ) )
        return
    
    origem = personagens[ numero - 1 ]
    alterar_rotulo( "Para quem a mensagem deve ser entregue?", rotulo )
    definir_acao( lambda : entregarMensagem3( origem, grafo, gerenciadorPersonagens, entrada, resultado, 
                rotulo, definir_acao, label_capa, label_grafoPlanetas, label_grafoPersonagens ) )

def entregarMensagem3( origem, grafo, gerenciadorPersonagens, entrada, resultado, rotulo, definir_acao, 
                     label_capa, label_grafoPlanetas, label_grafoPersonagens ):
    numero = ler_valor( entrada, rotulo )
    entrada.delete( 0, "end" )

    if numero is None:
        alterar_rotulo( "Opção inválida! Tente novamente:", rotulo )
        definir_acao( lambda : entregarMensagem3( origem, grafo,  gerenciadorPersonagens, entrada, resultado, 
                    rotulo, definir_acao, label_capa, label_grafoPlanetas, label_grafoPersonagens ) )
        return

    if numero < 1 or numero > len( personagens ) or personagens[ numero - 1 ] == origem:
        alterar_rotulo( "Opção inválida! Escolha outro personagem:", rotulo )
        definir_acao( lambda : entregarMensagem3( origem, grafo,  gerenciadorPersonagens, entrada, 
                    resultado, rotulo, definir_acao, label_capa, label_grafoPlanetas, label_grafoPersonagens ) )
        return

    destino = personagens[ numero - 1 ]

    alterar_rotulo( "Quantas mensagens devem ser entregues?", rotulo )
    definir_acao( lambda : entregarMensagem4( destino, origem, grafo, gerenciadorPersonagens, 
                entrada, resultado, rotulo, definir_acao, label_capa, label_grafoPlanetas, label_grafoPersonagens ) )

def entregarMensagem4( destino, origem, grafo, gerenciadorPersonagens, entrada, resultado, rotulo, 
                      definir_acao, label_capa, label_grafoPlanetas, label_grafoPersonagens ):
    qtd_mensagens = ler_valor( entrada, rotulo )
    entrada.delete( 0, "end" )

    if qtd_mensagens is None:
        alterar_rotulo( "Opção inválida! Tente novamente:", rotulo )
        definir_acao( lambda : entregarMensagem4( destino, origem, grafo, gerenciadorPersonagens,
                     entrada, resultado, rotulo, definir_acao, label_capa, label_grafoPlanetas, label_grafoPersonagens ) )
        return
    
    if qtd_mensagens <= 0:
        alterar_rotulo( "Informe uma quantidade maior que zero: ", rotulo )
        definir_acao( lambda : entregarMensagem4(destino, origem, grafo, gerenciadorPersonagens, 
                    entrada, resultado, rotulo, definir_acao, label_capa, label_grafoPlanetas, label_grafoPersonagens ) )
        return

    fluxo = ford_fulkerson( resultado, grafo, origem, destino )

    resultado.delete( "1.0", "end" )
    if qtd_mensagens > fluxo:
        resultado.insert( "end", "A mensagens não foram entregues\n" )
        resultado.insert( "end", f"Mensagens solicitadas: { qtd_mensagens }\n" )
        resultado.insert( "end", f"Fluxo máximo de mensagens: { fluxo }\n" )
    else:
        resultado.insert( "end", f"Sucesso no envio de { qtd_mensagens } mensagens!\n" )
        resultado.insert( "end", f"Remetente: { origem }\n" )
        resultado.insert( "end", f"Destinatário: { destino }\n" )
        resultado.insert( "end", f"Fluxo máximo de mensagens: { fluxo }\n" )