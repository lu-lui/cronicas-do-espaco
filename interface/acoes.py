from navegacao.funcoes_principais import ler_valor, limpar_terminal, alterar_rotulo

def selecionar_busca_nome(definir_acao, gerenciadorPersonagens, entrada, resultado, rotulo, label_capa, label_grafoPlanetas):
    limpar_terminal(label_grafoPlanetas, label_capa, resultado)

    alterar_rotulo("Digite o nome do personagem:", rotulo)
    definir_acao(lambda:pesquisar_personagem(gerenciadorPersonagens, entrada, resultado))
    return

def pesquisar_personagem(gerenciadorPersonagens, entrada, resultado):
    nome = entrada.get()
    entrada.delete(0, "end")
    personagem = gerenciadorPersonagens.buscar_nome(nome)

    #apagar oq estiver no resultado
    resultado.delete("1.0", "end")

    #end inserir texto no final do que já tiver
    if personagem is not None:
        resultado.insert("end", personagem)
    else:
        resultado.insert("end", "Personagem não encontrado.")
    return

def selecionar_busca_prefixo(definir_acao, gerenciadorPersonagens, entrada, resultado, rotulo, label_capa, label_grafoPlanetas):
    limpar_terminal(label_grafoPlanetas, label_capa, resultado)

    alterar_rotulo("Digite o prefixo que busca: ", rotulo)
    definir_acao(lambda:pesquisar_personagem_prefixo(definir_acao, gerenciadorPersonagens, entrada, resultado, rotulo))
    return

def pesquisar_personagem_prefixo(definir_acao, gerenciadorPersonagens, entrada, resultado, rotulo):
    prefixo = entrada.get()
    entrada.delete(0, "end")
    personagens = gerenciadorPersonagens.buscar_prefixo(prefixo)
    resultado.delete("1.0", "end")
    
    if personagens:
        i = 0
        for personagem in personagens:
            resultado.insert("end", str(i) + "." + personagem.name + "\n")
            i += 1

        alterar_rotulo("Qual resultado deseja imprimir?", rotulo)

        definir_acao(lambda: selecionar_personagem(personagens, entrada, resultado))
        return personagens

    else:
        resultado.insert("end", "Prefixo não encontrado.")
        return None

def selecionar_personagem(personagens, entrada, resultado):
    try:
        indice = int(entrada.get())
        entrada.delete(0, "end")

        if 0 <= indice < len(personagens):
            resultado.delete("1.0", "end")
            resultado.insert("end", personagens[indice])
        else:
            resultado.insert("end", "\nÍndice inválido.")

    except ValueError:
        resultado.insert("end", "\nDigite apenas números.")
    return

def listar_todos(gerenciadorPersonagens, gerenciadorPlanetas, tipo_busca, resultado, label_capa, label_grafoPlanetas):
    limpar_terminal(label_grafoPlanetas, label_capa, resultado)

    resultado.delete("1.0", "end")
    if tipo_busca == "personagens":
        for personagem in gerenciadorPersonagens:
            resultado.insert("end", str(personagem) + "\n")
    elif tipo_busca == "planetas":
        for planeta in gerenciadorPlanetas:
            resultado.insert("end", str(planeta) + "\n")
    return

def buscar_intervalo(gerenciadorPersonagens, gerenciadorPlanetas, definir_acao, tipo_busca, rotulo, entrada, resultado, label_capa, label_grafoPlanetas):
    limpar_terminal(label_grafoPlanetas, label_capa, resultado)

    alterar_rotulo("Digite o valor mínimo: ", rotulo)
    definir_acao(lambda : ler_valor_minimo(gerenciadorPersonagens, gerenciadorPlanetas, definir_acao, tipo_busca, entrada, resultado, rotulo))
    return

def ler_valor_minimo(gerenciadorPersonagens, gerenciadorPlanetas, definir_acao, tipo_busca, entrada, resultado, rotulo):
    minimo = ler_valor(entrada, rotulo)
    entrada.delete(0, "end")
    if minimo is not None:
        alterar_rotulo("Digite o valor máximo:", rotulo)
        definir_acao(lambda : ler_valor_maximo(gerenciadorPersonagens, gerenciadorPlanetas, tipo_busca, minimo, entrada, resultado, rotulo))

    return

def ler_valor_maximo(gerenciadorPersonagens, gerenciadorPlanetas, tipo_busca, minimo, entrada, resultado, rotulo):
    maximo = ler_valor(entrada, rotulo)
    entrada.delete(0, "end")
    resultado.delete("1.0", "end")
    if maximo is not None:
        if minimo <= maximo:
            if(tipo_busca == "peso"):
                elementos = gerenciadorPersonagens.buscar_intervalo_peso(minimo, maximo)
            elif(tipo_busca == "altura"):
                elementos = gerenciadorPersonagens.buscar_intervalo_altura(minimo, maximo)
            elif(tipo_busca == "diametro"):
                elementos = gerenciadorPlanetas.buscar_intervalo_diametro(minimo, maximo)
            elif(tipo_busca == "populacao"):
                elementos = gerenciadorPlanetas.buscar_intervalo_populacao(minimo, maximo)

            resultado.delete("1.0", "end")
            if elementos:
                for elemento in elementos:
                    resultado.insert("end", str(elemento) + "\n")
            else:
                resultado.insert("end", "Nenhum resultado encontrado.")
        else:
            resultado.insert("end", "O mínimo não pode ser maior que o máximo.")

    return

def pesquisar_valor(gerenciadorPersonagens, gerenciadorPlanetas, tipo_busca, entrada, resultado, definir_acao, rotulo, label_capa, label_grafoPlanetas):
    limpar_terminal(label_grafoPlanetas, label_capa, resultado)

    alterar_rotulo("Digite o valor que busca: ", rotulo)
    definir_acao(lambda: busca_valor(gerenciadorPersonagens, gerenciadorPlanetas, tipo_busca, entrada, resultado, rotulo))
    return

def busca_valor(gerenciadorPersonagens, gerenciadorPlanetas, tipo_busca, entrada, resultado, rotulo):
    valor = ler_valor(entrada, rotulo)
    entrada.delete(0, "end")

    if valor is None:
        return
    
    if tipo_busca == "peso":
        elementos = gerenciadorPersonagens.buscar_peso(valor)
    elif tipo_busca == "altura":
        elementos = gerenciadorPersonagens.buscar_altura(valor)
    elif tipo_busca == "diametro":
        elementos = gerenciadorPlanetas.buscar_diametro(valor)
    elif tipo_busca == "populacao":
        elementos = gerenciadorPlanetas.buscar_populacao(valor)
    
    resultado.delete("1.0", "end")
    if elementos:
        for elemento in elementos:
            resultado.insert("end", str(elemento) + "\n")
    else:
        resultado.insert("end", "Nenhum resultado encontrado.")

    return

def procurar_cor_olho(gerenciadorPersonagens, resultado, indice, label_capa, label_grafoPlanetas):
    limpar_terminal(label_grafoPlanetas, label_capa, resultado)

    cores = [ "black", "brown", "hazel", "blue", "yellow", "" ]
    resultado.delete("1.0", "end")
    flag = False
    for personagem in gerenciadorPersonagens:
        if indice == 1:
            if personagem.eye_color == cores[1] or personagem.eye_color == cores[2]:
                resultado.insert("end", str(personagem) + "\n")
                flag = True
        elif indice == -1:
            if personagem.eye_color not in cores:
                resultado.insert("end", str(personagem) + "\n")
                flag = True
        else:
            if personagem.eye_color == cores[indice]:
                resultado.insert("end", str(personagem) + "\n")
                flag = True

    if not flag:
        resultado.insert("end", "Nenhum resultado encontrado.\n")
    return

def procurar_genero(gerenciadorPersonagens, resultado, genero, label_capa, label_grafoPlanetas):
    limpar_terminal(label_grafoPlanetas, label_capa, resultado)

    resultado.delete("1.0", "end")
    flag = False
    for personagem in gerenciadorPersonagens:
        if personagem.gender == genero:
            resultado.insert("end", str(personagem) + "\n")
            flag = True
    if not flag:
        resultado.insert("end", "Nenhum resultado encontrado.\n")
    return

def procurar_homeworld(gerenciadorPersonagens, resultado, entrada, definir_acao, rotulo, label_capa, label_grafoPlanetas):
    limpar_terminal(label_grafoPlanetas, label_capa, resultado)
    alterar_rotulo("Digite o planeta de origem: ", rotulo)
    definir_acao(lambda:pesquisar_homeworld(gerenciadorPersonagens, resultado, entrada))

def pesquisar_homeworld(gerenciadorPersonagens, resultado, entrada):
    homeworld = entrada.get()
    homeworld = " ".join(homeworld.lower().split())
    entrada.delete(0, "end")
    resultado.delete("1.0", "end")
    flag = False
    for personagem in gerenciadorPersonagens:
        home = " ".join(personagem.homeworld.lower().split())
        if( home == homeworld ):
            resultado.insert("end", str(personagem) + "\n")
            flag = True
                    
    if not flag:                      
        resultado.insert("end", "Nenhum resultado encontrado.\n")


def selecionar_busca_nome_pla(definir_acao, gerenciadorPlanetas, entrada, resultado, rotulo, label_capa, label_grafoPlanetas):
    limpar_terminal(label_grafoPlanetas, label_capa, resultado)
    alterar_rotulo("Digite o nome do planeta:", rotulo)
    definir_acao(lambda:pesquisar_planeta(gerenciadorPlanetas, entrada, resultado))
    return

def pesquisar_planeta(gerenciadorPlanetas, entrada, resultado):
    nome = entrada.get()
    entrada.delete(0, "end")
    planeta = gerenciadorPlanetas.buscar_nome(nome)

    #apagar oq estiver no resultado
    resultado.delete("1.0", "end")

    #end inserir texto no final do que já tiver
    if planeta is not None:
        resultado.insert("end", planeta)
    else:
        resultado.insert("end", "Planeta não encontrado.")
    return

def selecionar_busca_prefixo_plan(definir_acao, gerenciadorPlanetas, entrada, resultado, rotulo, label_capa, label_grafoPlanetas):
    limpar_terminal(label_grafoPlanetas, label_capa, resultado)
    alterar_rotulo("Digite o prefixo que busca: ", rotulo)
    definir_acao(lambda:pesquisar_planeta_prefixo(definir_acao, gerenciadorPlanetas, entrada, resultado, rotulo))
    return

def pesquisar_planeta_prefixo(definir_acao, gerenciadorPlanetas, entrada, resultado, rotulo):
    prefixo = entrada.get()
    entrada.delete(0, "end")
    planetas = gerenciadorPlanetas.buscar_prefixo(prefixo)
    resultado.delete("1.0", "end")
    
    if planetas:
        i = 0
        for planeta in planetas:
            resultado.insert("end", str(i) + "." + planeta.name + "\n")
            i += 1

        alterar_rotulo("Qual resultado deseja imprimir?", rotulo)

        definir_acao(lambda: selecionar_planeta(planetas, entrada, resultado))
        return planetas

    else:
        resultado.insert("end", "Prefixo não encontrado.")
        return None

def selecionar_planeta(planetas, entrada, resultado):
    try:
        indice = int(entrada.get())
        entrada.delete(0, "end")

        if 0 <= indice < len(planetas):
            resultado.delete("1.0", "end")
            resultado.insert("end", planetas[indice])
        else:
            resultado.insert("end", "\nÍndice inválido.")

    except ValueError:
        resultado.insert("end", "\nDigite apenas números.")
    return

def filtrar_clima(gerenciadorPlanetas, resultado, clima, label_capa, label_grafoPlanetas):
    limpar_terminal(label_grafoPlanetas, label_capa, resultado)
    climas = ["temperate", "arid", "tropical", "hot"]
    flag = False
    resultado.delete("1.0", "end")
    for planeta in gerenciadorPlanetas:
        if clima == -1:
            if planeta.climate not in climas:
                resultado.insert("end", str(planeta) + "\n")
                flag = True
        else:
            if planeta.climate == climas[clima]:
                resultado.insert("end", str(planeta) + "\n")
                flag = True

    if not flag:
        resultado.insert("end", "Nenhum planeta encontrado com esse clima.")
    return

def filtrar_gravidade(definir_acao, gerenciadorPlanetas, entrada, rotulo, resultado, label_capa, label_grafoPlanetas):
    limpar_terminal(label_grafoPlanetas, label_capa, resultado)
    alterar_rotulo("Digite a gravidade que busca: ", rotulo)
    definir_acao(lambda:gravidade(gerenciadorPlanetas, entrada, resultado, rotulo))
    return

def gravidade(gerenciadorPlanetas, entrada, resultado, rotulo):
    gravidade = entrada.get()
    entrada.delete(0, "end")
    flag = False
    resultado.delete("1.0", "end")
    for planeta in gerenciadorPlanetas:
        if planeta.gravity == gravidade:
            resultado.insert("end", str(planeta) + "\n")
            flag = True
    if not flag:
        resultado.insert("end", "Nenhum planeta encontrado com essa gravidade.")
    return