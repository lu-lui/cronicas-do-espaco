def limpar_terminal(label_grafoPlanetas, label_capa, resultado):
    label_grafoPlanetas.pack_forget()
    label_capa.pack_forget()
    resultado.delete("1.0", "end")

def ler_valor(entrada, rotulo):
    try:
        return int(entrada.get())
    except ValueError:
        alterar_rotulo("Digite apenas números", rotulo)
        return None

def alterar_rotulo(texto, rotulo_entrada):
    rotulo_entrada.config(text=texto)
    return

planetas_missao = ["Alderaan", "Cerea", "Chandrila", "Corellia", "Coruscant", "Kashyyyk", "Malastare", "Naboo", "Shili", "Umbara"]

def mostrarPlanetas(resultado):
    i = 1
    resultado.delete("1.0", "end")
    for nome in planetas_missao:
        resultado.insert("end", f"{i} - {nome}\n")
        i += 1

def exibir(grafo, rota, custo, destinos):
    return f"Roteiro da viagem: {' -> '.join(rota)}\nCusto: {custo}"
