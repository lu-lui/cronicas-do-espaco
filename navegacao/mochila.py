from .caixeiro_viajante import criar_grafo, roteiro_missao, exibir
from .funcoes_principais import ler_valor, limpar_terminal, alterar_rotulo

#MISSAO 1
def viagem_mochila( gerenciadorPersonagens, gerenciadorPlanetas, entrada, resultado, rotulo, definir_acao, label_capa, label_grafoPlanetas, label_grafoPersonagens):
    limpar_terminal(label_grafoPersonagens, label_grafoPlanetas, label_capa, resultado)
    resultado.insert("end", "Vamos planejar uma viagem espacial, vamos ver quantas pessoas podemos levar de seu planeta de origem a outro conforme a capacidade da nave!\n")
    alterar_rotulo("Digite o planeta de saída: ", rotulo)
    definir_acao(lambda : planeta_saida(gerenciadorPersonagens, gerenciadorPlanetas, entrada, resultado, rotulo, definir_acao))
    return

def planeta_saida(gerenciadorPersonagens, gerenciadorPlanetas, entrada, resultado, rotulo, definir_acao):
    planetaSaida = entrada.get()
    entrada.delete(0, "end")

    if not gerenciadorPlanetas.e_planeta(planetaSaida):
            alterar_rotulo(f"{planetaSaida} não é um planeta real\n Digite um planeta real.\n", rotulo)
            definir_acao(lambda : planeta_saida(gerenciadorPersonagens, gerenciadorPlanetas, entrada, resultado, rotulo, definir_acao))
            return
    
    planetaSaida = " ".join(planetaSaida.lower().split())
    alterar_rotulo("Digite o planeta destino: ", rotulo)
    definir_acao(lambda : planeta_destino(gerenciadorPersonagens, gerenciadorPlanetas, entrada, resultado, rotulo, definir_acao, planetaSaida))
    return

def planeta_destino(gerenciadorPersonagens, gerenciadorPlanetas, entrada, resultado, rotulo, definir_acao, planetaSaida):
    planetaDestino = entrada.get()
    entrada.delete(0, "end")

    if not gerenciadorPlanetas.e_planeta(planetaDestino):
        alterar_rotulo(f"{planetaDestino} não é um planeta real\n Digite um planeta real.\n", rotulo)
        definir_acao(lambda : planeta_destino(gerenciadorPersonagens, gerenciadorPlanetas, entrada, resultado, rotulo, definir_acao, planetaSaida))
        return

    planetaDestino = " ".join(planetaDestino.lower().split())
    alterar_rotulo("Digite a capacidade da nave (kg): ", rotulo)
    definir_acao(lambda : capacidade_nave(gerenciadorPersonagens, entrada, resultado, planetaSaida, planetaDestino, rotulo))
    return

def capacidade_nave(gerenciadorPersonagens, entrada, resultado, planetaSaida, planetaDestino, rotulo):
    capacidade = ler_valor(entrada, rotulo)
    entrada.delete(0, "end")
    pessoasPossiveis = []

    for personagem in gerenciadorPersonagens:
        if personagem.mass != "unknown":
            home = " ".join(personagem.homeworld.lower().split())
            if home == planetaSaida:
                pessoasPossiveis.append( personagem )

    pessoasPossiveisOrdenadas = sorted( pessoasPossiveis, key=lambda p: float( p.mass.replace( ",", "" ) ) )

    cargaNave = 0
    tamVetor = len( pessoasPossiveisOrdenadas )
    pessoasQueVao = []
    i = 0
    contPessoas = 0

    if capacidade is None:
        return

    while i < tamVetor:
        peso = float( pessoasPossiveisOrdenadas[ i ].mass.replace( ",", "" ) )
        if cargaNave + peso <= capacidade:
            pessoasQueVao.append( pessoasPossiveisOrdenadas[ i ] )
            cargaNave += peso
            contPessoas += 1
            i += 1
        else:
            break

    resultado.delete("1.0", "end")
    resultado.insert("end", f"Vamos levar { contPessoas } pessoas de { planetaSaida.title() } para { planetaDestino.title() }!\n" )
    resultado.insert("end", "Lista de passageiros:\n" )
    i = 0
    for personagem in pessoasQueVao:
        i += 1
        resultado.insert( "end", f"{i}: {personagem.name}\n" )

    return