from .caixeiro_viajante import criar_grafo
from .funcoes_principais import alterar_rotulo, limpar_terminal, ler_valor, mostrarPlanetas

planetas_missao = [ "Alderaan", "Cerea", "Chandrila", "Corellia", "Coruscant", 
                   "Kashyyyk", "Malastare", "Naboo", "Shili", "Umbara" ]

def achar_ciclo_dfs( subgrafo, origem ):
    cor = {}
    for planeta in subgrafo:
        cor[ planeta ] = "branco" #branco == ainda não visitado
    caminho = []

    def visitar( atual ):
        cor[ atual ] = "cinza" #cinza == visitado (em processamento)
        caminho.append( atual )

        for vizinho in subgrafo[ atual ]:
            if cor[ vizinho ] == "cinza":
                inicio = caminho.index( vizinho )
                return caminho[inicio:] + [ vizinho ]
            if cor[ vizinho ] == "branco":
                ciclo = visitar( vizinho )
                if ciclo is not None:
                    return ciclo

        caminho.pop()
        cor[ atual ] = "preto" #preto == processado e finalizado
        return None
    
    return visitar( origem )

def verificarCiclos1( gerenciadorPlanetas, entrada, resultado, rotulo, definir_acao, 
                     label_capa, label_grafoPlanetas, label_grafoPersonagens ):
    
    limpar_terminal( label_grafoPersonagens, label_grafoPlanetas, label_capa, resultado )
    grafo = criar_grafo( gerenciadorPlanetas, planetas_missao )
    resultado.pack_forget()
    label_grafoPlanetas.pack( anchor = "n" )
    resultado.pack( side = "left", fill = "both", expand = True )

    mostrarPlanetas( resultado )
    resultado.insert( "end", "O gps de uma nova nave ainda não foi configurado completamente e caso encontre algum ciclo no trajeto ele se perde. Vamos escolher um trajeto e verificar se no trajeto escolhido encontramos algum ciclo que pode fazer a nave se perder!" )
    alterar_rotulo( "Escolha o planeta de origem: ", rotulo )
    definir_acao( lambda : verificarCiclos2( grafo, entrada, resultado, rotulo, definir_acao ) )

def verificarCiclos2( grafo, entrada, resultado, rotulo, definir_acao ):
    numero = ler_valor( entrada, rotulo )
    entrada.delete( 0, "end" )

    if numero is None:
        definir_acao( lambda : verificarCiclos2( grafo, entrada, resultado, rotulo, definir_acao ) )
        return

    if numero < 1 or numero > 10:
        alterar_rotulo( "Opção inválida! Tente novamente: ", rotulo )
        definir_acao( lambda : verificarCiclos2( grafo, entrada, resultado, rotulo, definir_acao ) )
        return
    
    origem = planetas_missao[ numero - 1 ]
    subgrafo = {}
    for nome in planetas_missao:
        subgrafo[ nome ] = []
    trajeto = [ origem ]
    atual = origem

    verificarCiclos3( origem, grafo, subgrafo, trajeto, atual, entrada, resultado, rotulo, definir_acao )

def verificarCiclos3( origem, grafo, subgrafo, trajeto, atual, entrada, resultado, rotulo, definir_acao ):
    vizinhos = list( grafo.adjacencia[ atual ] )

    resultado.delete( "1.0", "end" )
    resultado.insert( "end", f"\nTrajeto até agora: { ' -> '.join( trajeto ) }\nRotas diretas a partir de { atual }:\n" )

    i = 1
    for nome in vizinhos:
        resultado.insert( "end", f"{ i } - { nome }\n" )
        i += 1

    alterar_rotulo( "Para qual planeta deseja ir? (0 para terminar): ", rotulo )
    definir_acao( lambda : verificarCiclos4( origem, grafo, subgrafo, trajeto, 
                atual, vizinhos, entrada, resultado, rotulo, definir_acao ) )

def verificarCiclos4( origem, grafo, subgrafo, trajeto, atual, vizinhos, entrada, 
                     resultado, rotulo, definir_acao ):
    numero = ler_valor( entrada, rotulo )
    entrada.delete( 0, "end" )

    if numero is None:
        definir_acao( lambda : verificarCiclos4( origem, grafo, subgrafo, trajeto, atual, 
                    vizinhos,entrada, resultado, rotulo, definir_acao ) )
        return

    if numero == 0:
        if len( trajeto ) > 1:
            ciclo = achar_ciclo_dfs( subgrafo, origem )
            resultado.delete( "1.0", "end" )
            if ciclo is None:
                resultado.insert( "end", "\nNenhum ciclo foi encontrado!\nA nave não se perdeu!" )
            else:
                resultado.insert( "end", f"\nCiclo encontrado: { ' -> '.join( ciclo ) }\nAh não! A nave se perdeu..." )
            return 

        alterar_rotulo( "Escolha pelo menos um planeta.", rotulo )
        definir_acao( lambda : verificarCiclos3( origem, grafo, subgrafo, trajeto, atual, 
                    entrada, resultado, rotulo, definir_acao ) )
        return

    if numero < 0 or numero > len( vizinhos ):
        alterar_rotulo( "Opção Inválida", rotulo )
        definir_acao( lambda : verificarCiclos3( origem, grafo, subgrafo, trajeto, atual,
                    entrada, resultado, rotulo, definir_acao ) )
        return

    proximo = vizinhos[ numero - 1 ]
    if proximo not in subgrafo[ atual ]:
        subgrafo[ atual ].append( proximo )

    trajeto.append( proximo )
    atual = proximo

    verificarCiclos3( origem, grafo, subgrafo, trajeto, atual,entrada, resultado, rotulo, definir_acao )