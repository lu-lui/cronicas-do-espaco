def ler_valor(entrada, resultado):
    try:
        return int(entrada.get())
    except ValueError:
        resultado.insert("end", "Digite apenas números\n")
        return None

def alterar_rotulo(texto, rotulo_entrada):
    rotulo_entrada.config(text=texto)
    return

def viagem_mochila( gerenciadorPersonagens, entrada, resultado, rotulo, definir_acao, label_capa ):
    label_capa.pack_forget()
    alterar_rotulo("Digite o planeta de saída: ", rotulo)
    definir_acao(lambda : planeta_saida(gerenciadorPersonagens, entrada, resultado, rotulo, definir_acao))
    return

def planeta_saida(gerenciadorPersonagens, entrada, resultado, rotulo, definir_acao):
    planetaSaida = entrada.get()
    entrada.delete(0, "end")
    planetaSaida = " ".join(planetaSaida.lower().split())
    alterar_rotulo("Digite o planeta destino: ", rotulo)
    definir_acao(lambda : planeta_destino(gerenciadorPersonagens, entrada, resultado, rotulo, definir_acao, planetaSaida))
    return

def planeta_destino(gerenciadorPersonagens, entrada, resultado, rotulo, definir_acao, planetaSaida):
    planetaDestino = entrada.get()
    entrada.delete(0, "end")
    planetaDestino = " ".join(planetaDestino.lower().split())
    alterar_rotulo("Digite a capacidade da nave (kg): ", rotulo)
    definir_acao(lambda : capacidade_nave(gerenciadorPersonagens, entrada, resultado, planetaSaida, planetaDestino))
    return

def capacidade_nave(gerenciadorPersonagens, entrada, resultado, planetaSaida, planetaDestino):
    capacidade = ler_valor(entrada, resultado)
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