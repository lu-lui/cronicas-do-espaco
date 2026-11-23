def viagemEspacial( gerenciadorPersonagens, planetaSaida, planetaDestino, capacidade ):
    pessoasPossiveis = []

    for personagem in gerenciadorPersonagens:
        if personagem.mass != "unknown":
            if personagem.homeworld == planetaSaida:
                pessoasPossiveis.append( personagem )

    pessoasPossiveisOrdenadas = sorted( pessoasPossiveis, key=lambda p: float( p.mass.replace( ",", "" ) ) )

    cargaNave = 0
    tamVetor = len( pessoasPossiveisOrdenadas )
    pessoasQueVao = []
    i = 0
    contPessoas = 0

    while i < tamVetor:
        peso = float( pessoasPossiveisOrdenadas[ i ].mass.replace( ",", "" ) )
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
        print( i, ":", personagem.name )

    return