import tkinter as tk
from PIL import Image, ImageTk #pras imagens - pip install pillow
from .acoes import selecionar_busca_nome, selecionar_busca_prefixo, listar_todos, buscar_intervalo, pesquisar_valor, procurar_cor_olho, procurar_genero, procurar_homeworld, selecionar_busca_nome_pla, selecionar_busca_prefixo_plan, filtrar_clima, filtrar_gravidade
from .missoes import viagem_mochila

#janela principal
def criar_janela(gerenciadorPersonagens, gerenciadorPlanetas):
    janela = tk.Tk()        #cria a janela
    janela.title("Star Wars")
    janela.geometry("900x600")
    #frames dentro da janela
    menu = tk.Frame(janela, bg="#252A38")
    painel = tk.Frame(janela, bg="#171923")
    #grid() organiza os elementos em linhas e colunas 
    #sticky=nsew é pro frame se expandir em todas direções
    menu.grid(row = 0, column=0, sticky="nsew")
    painel.grid(row=0, column=1, sticky="nsew")
    menu.grid_propagate(False)
    painel.grid_propagate(False)
    #organiza a proporção das colunas 
    janela.grid_columnconfigure(0, weight=4, uniform="colunas")
    janela.grid_columnconfigure(1, weight=6, uniform="colunas")
    janela.grid_rowconfigure(0, weight=1)
    acao_atual = None

    capa = Image.open("imagens/capa_star_wars.jpg")
    capa = capa.resize((600, 400))
    capa_tk = ImageTk.PhotoImage(capa)
    label_capa = tk.Label(painel, image=capa_tk, bg="#171923")
    label_capa.image = capa_tk  #guardar referência
    label_capa.pack(anchor="n")

    #Funções Intermediárias
    def definir_acao(nova_acao):
        nonlocal acao_atual
        acao_atual = nova_acao

    def executar_acao(event=None):
        if acao_atual is not None:
            acao_atual()

        #caixa de entrada
    
    #insertbackground cor cursor
    entrada = tk.Entry(menu, bg="#001963", fg="white", insertbackground="white", 
            font=("Consolas", 11))
    entrada.pack(side="bottom", pady=10, fill = "x", ipady=5)
    entrada.bind("<Return>", executar_acao)
    rotulo = tk.Label(menu, text="Selecione uma opção", bg="#252A38", fg="white", font=("Consolas", 11))
    rotulo.pack(side="bottom", pady=(5, 0))

    #painel com resultados / terminal
    #wrap="word" quebra as linhas quando o texto chega ao limite, evitando que palavras fiquem cortadas
    resultado = tk.Text(painel, bg="#171923", fg="white", font=("Consolas", 11), wrap="word")
    resultado.pack(side = "left", fill="both", expand=True)

    resultado.insert("end", "PERSONAGENS:\n" + gerenciadorPersonagens.exibir_informacoes() + "\n")
    resultado.insert("end", "\nPLANETAS:\n" + gerenciadorPlanetas.exibir_informacoes())

    #botões:
    #pack organiza os botões um embaixo do outro
    #pady - espaçamento vertical
    #bg - cor fundo
    #fg - cor texto
    #fill x - ocupar largura
    #ipady altura dos botões

    #PERSONAGENS
    opcoes_personagens = tk.Frame(menu, bg="#252A38")
    opcoes_filtros_pers = tk.Frame(opcoes_personagens, bg="#252A38")
    opcoes_peso = tk.Frame(opcoes_filtros_pers, bg="#252A38")
    opcoes_altura = tk.Frame(opcoes_filtros_pers, bg="#252A38")
    opcoes_genero = tk.Frame(opcoes_filtros_pers, bg="#252A38")
    opcoes_cor_olhos = tk.Frame(opcoes_filtros_pers, bg="#252A38")

    def mostrar_personagens():
        if opcoes_personagens.winfo_ismapped(): #se o frame ta aparecendo na tela esconde
            opcoes_personagens.pack_forget()
        else:
            opcoes_personagens.pack(fill="x", before=botao_planetas) #se nn ta mostra ele

    def restaurar_lista_filtros_pers():
        #fechar submenus
        opcoes_peso.pack_forget()
        opcoes_altura.pack_forget()
        opcoes_genero.pack_forget()
        opcoes_cor_olhos.pack_forget()

        #fechar todos botoes do filtro
        botao_listar_todos.pack_forget()
        botao_filtrar_peso.pack_forget()
        botao_filtrar_altura.pack_forget()
        botao_filtrar_genero.pack_forget()
        botao_filtrar_cor_olhos.pack_forget()
        botao_filtrar_por_planeta.pack_forget()

        #colocar botoes de volta na ordem
        botao_listar_todos.pack(fill="x", pady=3)
        botao_filtrar_peso.pack(fill="x", pady=3)
        botao_filtrar_altura.pack(fill="x", pady=3)
        botao_filtrar_genero.pack(fill="x", pady=3)
        botao_filtrar_cor_olhos.pack(fill="x", pady=3)
        botao_filtrar_por_planeta.pack(fill="x", pady=3)
        
    def filtros_personagens():
        if opcoes_filtros_pers.winfo_ismapped(): #se o frame ta aparecendo na tela esconde
            opcoes_filtros_pers.pack_forget()

            botao_buscar_nome_pers.pack(fill="x", pady=3, before=botao_filtrar_personagens)
            botao_buscar_prefixo_pers.pack(fill="x", pady=3, before=botao_filtrar_personagens)
        else:
            botao_buscar_nome_pers.pack_forget()
            botao_buscar_prefixo_pers.pack_forget()
            
            opcoes_filtros_pers.pack(fill="x") #se nn ta mostra ele

    def filtros_peso():
        if opcoes_peso.winfo_ismapped():
            restaurar_lista_filtros_pers()

        else:
            botao_listar_todos.pack_forget()
            botao_filtrar_altura.pack_forget()
            botao_filtrar_genero.pack_forget()
            botao_filtrar_cor_olhos.pack_forget()
            botao_filtrar_por_planeta.pack_forget()

            opcoes_peso.pack(fill="x")

    def filtros_altura():
        if opcoes_altura.winfo_ismapped():
            restaurar_lista_filtros_pers()
        else:
            botao_listar_todos.pack_forget()
            botao_filtrar_peso.pack_forget()
            botao_filtrar_genero.pack_forget()
            botao_filtrar_cor_olhos.pack_forget()
            botao_filtrar_por_planeta.pack_forget()

            opcoes_altura.pack(fill="x")

    def filtros_genero():
        if opcoes_genero.winfo_ismapped():
            restaurar_lista_filtros_pers()
        else:
            botao_listar_todos.pack_forget()
            botao_filtrar_peso.pack_forget()
            botao_filtrar_altura.pack_forget()
            botao_filtrar_cor_olhos.pack_forget()
            botao_filtrar_por_planeta.pack_forget()

            opcoes_genero.pack(fill="x")

    def filtros_olhos():
        if opcoes_cor_olhos.winfo_ismapped():
            restaurar_lista_filtros_pers()
        else:
            botao_listar_todos.pack_forget()
            botao_filtrar_peso.pack_forget()
            botao_filtrar_altura.pack_forget()
            botao_filtrar_genero.pack_forget()
            botao_filtrar_por_planeta.pack_forget()

            opcoes_cor_olhos.pack(fill="x")

    botao_personagens = tk.Button(menu, text="Personagens", bg="#001963", fg="white", command=mostrar_personagens)
    #->
    botao_buscar_nome_pers = tk.Button(opcoes_personagens, text="Pesquisar por nome", bg="#343B50", fg="white", 
                                       command=lambda :selecionar_busca_nome(definir_acao, gerenciadorPersonagens, entrada, resultado, rotulo, label_capa))
    botao_buscar_prefixo_pers = tk.Button(opcoes_personagens, text="Pesquisar por prefixo", bg="#343B50", fg="white", 
                                          command=lambda :selecionar_busca_prefixo(definir_acao, gerenciadorPersonagens, entrada, resultado, rotulo, label_capa))
    botao_filtrar_personagens = tk.Button(opcoes_personagens, text="Filtrar personagens", bg="#343B50", fg="white", 
                                          command=filtros_personagens)
    #-->
    botao_listar_todos = tk.Button(opcoes_filtros_pers, text="Listar todos", bg="#37487B", fg="white", 
                                   command=lambda :listar_todos(gerenciadorPersonagens, gerenciadorPlanetas, "personagens", resultado, label_capa))
    botao_filtrar_peso = tk.Button(opcoes_filtros_pers, text="Filtrar por peso", bg="#37487B", fg="white", 
                                   command=filtros_peso)
    botao_filtrar_altura = tk.Button(opcoes_filtros_pers, text="Filtrar por altura", bg="#37487B", fg="white", 
                                     command=filtros_altura)
    botao_filtrar_genero = tk.Button(opcoes_filtros_pers, text="Filtrar por gênero", bg="#37487B", fg="white", 
                                     command=filtros_genero)
    botao_filtrar_cor_olhos = tk.Button(opcoes_filtros_pers, text="Filtrar por cor dos olhos", bg="#37487B", fg="white", 
                                        command=filtros_olhos)
    botao_filtrar_por_planeta = tk.Button(opcoes_filtros_pers, text="Filtrar por planeta", bg="#37487B", fg="white",
                                          command = lambda : procurar_homeworld(gerenciadorPersonagens, resultado, entrada, definir_acao, rotulo, label_capa))
    #---> peso
    botao_peso_intervalo = tk.Button(opcoes_peso, text="Filtrar por intervalo", bg="#002699", fg="white", 
                                     command=lambda :buscar_intervalo(gerenciadorPersonagens, gerenciadorPlanetas, definir_acao, "peso", rotulo, entrada, resultado, label_capa))
    botao_peso_exato = tk.Button(opcoes_peso, text="Filtrar por valor exato", bg="#002699", fg="white", 
                                 command=lambda : pesquisar_valor(gerenciadorPersonagens, gerenciadorPlanetas, "peso", entrada, resultado, definir_acao, rotulo, label_capa))
    #--->altura
    botao_altura_intervalo = tk.Button(opcoes_altura, text="Filtrar por intervalo", bg="#002699", fg="white", 
                                       command=lambda :buscar_intervalo(gerenciadorPersonagens, gerenciadorPlanetas, definir_acao, "altura", rotulo, entrada, resultado, label_capa))
    botao_altura_exato = tk.Button(opcoes_altura, text="Filtrar por valor exato", bg="#002699", fg="white", 
                                   command=lambda : pesquisar_valor(gerenciadorPersonagens, gerenciadorPlanetas, "altura", entrada, resultado, definir_acao, rotulo, label_capa))
    #--->genero
    botao_genero_f = tk.Button(opcoes_genero, text="Feminino", bg="#002699", fg="white", 
                               command = lambda : procurar_genero(gerenciadorPersonagens, resultado, "female", label_capa))
    botao_genero_m = tk.Button(opcoes_genero, text="Masculino", bg="#002699", fg="white",
                               command = lambda : procurar_genero(gerenciadorPersonagens, resultado, "male", label_capa))
    #--->cor dos olhos
    botao_olho_preto = tk.Button(opcoes_cor_olhos, text="Preto", bg="#002699", fg="white",
                                 command = lambda : procurar_cor_olho(gerenciadorPersonagens, resultado, 0, label_capa))
    botao_olho_castanho = tk.Button(opcoes_cor_olhos, text="Castanho", bg="#002699", fg="white",
                                    command = lambda : procurar_cor_olho(gerenciadorPersonagens, resultado, 1, label_capa))
    botao_olho_azul = tk.Button(opcoes_cor_olhos, text="Azul", bg="#002699", fg="white",
                                command = lambda : procurar_cor_olho(gerenciadorPersonagens, resultado, 3, label_capa))
    botao_olho_amarelo = tk.Button(opcoes_cor_olhos, text="Amarelo", bg="#002699", fg="white",
                                   command = lambda : procurar_cor_olho(gerenciadorPersonagens, resultado, 4, label_capa))
    botao_olho_colorido = tk.Button(opcoes_cor_olhos, text="Colorido", bg="#002699", fg="white",
                                    command = lambda : procurar_cor_olho(gerenciadorPersonagens, resultado, -1, label_capa))
    
    botao_personagens.pack(pady = 5, fill="x", ipady=8)
    botao_buscar_nome_pers.pack(fill="x", pady=4)
    botao_buscar_prefixo_pers.pack(fill="x", pady=4)
    botao_filtrar_personagens.pack(fill="x", pady=4)
    botao_listar_todos.pack(fill="x", pady=3)
    botao_filtrar_peso.pack(fill="x", pady=3)
    botao_filtrar_altura.pack(fill="x", pady=3)
    botao_filtrar_genero.pack(fill="x", pady=3)
    botao_filtrar_cor_olhos.pack(fill="x", pady=3)
    botao_filtrar_por_planeta.pack(fill="x", pady=3)
    botao_peso_exato.pack(fill="x", pady=3)
    botao_peso_intervalo.pack(fill="x", pady=3)
    botao_altura_exato.pack(fill="x", pady=3)
    botao_altura_intervalo.pack(fill="x", pady=3)
    botao_genero_f.pack(fill="x", pady=3)
    botao_genero_m.pack(fill="x", pady=3)
    botao_olho_preto.pack(fill="x", pady=3)
    botao_olho_castanho.pack(fill="x", pady=3)
    botao_olho_azul.pack(fill="x", pady=3)
    botao_olho_amarelo.pack(fill="x", pady=3)
    botao_olho_colorido.pack(fill="x", pady=3)

    #PLANETAS
    opcoes_planetas = tk.Frame(menu, bg="#252A38")
    opcoes_filtros_planetas = tk.Frame(opcoes_planetas, bg="#252A38")
    opcoes_clima = tk.Frame(opcoes_filtros_planetas, bg="#252A38")
    opcoes_diametro = tk.Frame(opcoes_filtros_planetas, bg="#252A38")
    opcoes_populacao = tk.Frame(opcoes_filtros_planetas, bg="#252A38")

    def mostrar_planetas():
        if opcoes_planetas.winfo_ismapped(): #se o frame ta aparecendo na tela esconde
            opcoes_planetas.pack_forget()
        else:
            opcoes_planetas.pack(fill="x", before=botao_missoes) #se nn ta mostra ele

    def restaurar_lista_filtros_pla():
        #fechar submenus
        opcoes_clima.pack_forget()
        opcoes_diametro.pack_forget()
        opcoes_populacao.pack_forget()

        #fechar todos botoes do filtro
        botao_listar_todosPlanetas.pack_forget()
        botao_filtrar_clima.pack_forget()
        botao_filtrar_diametro.pack_forget()
        botao_filtrar_gravidade.pack_forget()
        botao_filtrar_populacao.pack_forget()

        #colocar botoes de volta na ordem
        botao_listar_todosPlanetas.pack(fill="x", pady=3)
        botao_filtrar_clima.pack(fill="x", pady=3)
        botao_filtrar_diametro.pack(fill="x", pady=3)
        botao_filtrar_gravidade.pack(fill="x", pady=3)
        botao_filtrar_populacao.pack(fill="x", pady=3)

    def filtros_planetas():
        if opcoes_filtros_planetas.winfo_ismapped(): #se o frame ta aparecendo na tela esconde
            botao_buscar_nome_plan.pack(fill="x", pady=3, before=botao_filtrar_planetas)
            botao_buscar_prefixo_plan.pack(fill="x", pady=3, before=botao_filtrar_planetas)
            opcoes_filtros_planetas.pack_forget()
        else:
            botao_buscar_nome_plan.pack_forget()
            botao_buscar_prefixo_plan.pack_forget()
            opcoes_filtros_planetas.pack(fill="x") #se nn ta mostra ele

    def filtros_clima():
        if opcoes_clima.winfo_ismapped():
            restaurar_lista_filtros_pla()

        else:
            botao_listar_todosPlanetas.pack_forget()
            botao_filtrar_diametro.pack_forget()
            botao_filtrar_gravidade.pack_forget()
            botao_filtrar_populacao.pack_forget()

            opcoes_clima.pack(fill="x")

    def filtros_diametro():
        if opcoes_diametro.winfo_ismapped():
            restaurar_lista_filtros_pla()

        else:
            botao_listar_todosPlanetas.pack_forget()
            botao_filtrar_clima.pack_forget()
            botao_filtrar_gravidade.pack_forget()
            botao_filtrar_populacao.pack_forget()

            opcoes_diametro.pack(fill="x")

    def filtros_populacao():
        if opcoes_populacao.winfo_ismapped():
            restaurar_lista_filtros_pla()

        else:
            botao_listar_todosPlanetas.pack_forget()
            botao_filtrar_clima.pack_forget()
            botao_filtrar_diametro.pack_forget()
            botao_filtrar_gravidade.pack_forget()

            opcoes_populacao.pack(fill="x")

    botao_planetas = tk.Button(menu, text="Planetas", bg="#001963", fg="white", command=mostrar_planetas)
    botao_buscar_nome_plan = tk.Button(opcoes_planetas, text="Buscar por nome", bg="#343B50", fg="white", command= lambda :selecionar_busca_nome_pla(definir_acao, gerenciadorPlanetas, entrada, resultado, rotulo, label_capa))
    botao_buscar_prefixo_plan = tk.Button(opcoes_planetas, text="Buscar por prefixo", bg="#343B50", fg="white", command=lambda :selecionar_busca_prefixo_plan(definir_acao, gerenciadorPlanetas, entrada, resultado, rotulo, label_capa))
    botao_filtrar_planetas = tk.Button(opcoes_planetas, text="Filtrar Planetas", bg="#343B50", fg="white", command=filtros_planetas)
    
    botao_listar_todosPlanetas = tk.Button(opcoes_filtros_planetas, text="Listar todos", bg="#37487B", fg="white", command = lambda : listar_todos(gerenciadorPersonagens, gerenciadorPlanetas, "planetas", resultado, label_capa))

    botao_filtrar_clima = tk.Button(opcoes_filtros_planetas, text="Filtrar por clima", bg="#37487B", fg="white", command = filtros_clima)
    botao_clima_temperado = tk.Button(opcoes_clima, text="Temperado", bg="#002699", fg="white", command=lambda : filtrar_clima(gerenciadorPlanetas, resultado, 0, label_capa))
    botao_clima_arido = tk.Button(opcoes_clima, text="Arido", bg="#002699", fg="white",
                                  command=lambda:filtrar_clima(gerenciadorPlanetas, resultado, 1, label_capa))
    botao_clima_tropical = tk.Button(opcoes_clima, text="Tropical", bg="#002699", fg="white", command=lambda : filtrar_clima(gerenciadorPlanetas, resultado, 2, label_capa))
    botao_clima_quente = tk.Button(opcoes_clima, text="Quente", bg="#002699",fg="white", command=lambda : filtrar_clima(gerenciadorPlanetas, resultado, 3, label_capa))
    botao_clima_outros = tk.Button(opcoes_clima, text="Outros", bg="#002699", fg="white", command=lambda: filtrar_clima(gerenciadorPlanetas, resultado, -1, label_capa))

    botao_filtrar_diametro = tk.Button(opcoes_filtros_planetas, text="Filtrar por diâmetro", bg="#37487B", fg="white", command= filtros_diametro)
    botao_diametro_intervalo = tk.Button(opcoes_diametro, text="Filtrar por intervalo", bg="#002699", fg="white", 
                                     command=lambda :buscar_intervalo(gerenciadorPersonagens, gerenciadorPlanetas, definir_acao, "diametro", rotulo, entrada, resultado, label_capa))
    botao_diametro_exato = tk.Button(opcoes_diametro, text="Filtrar por valor exato", bg="#002699", fg="white", 
                                 command=lambda : pesquisar_valor(gerenciadorPersonagens, gerenciadorPlanetas, "diametro", entrada, resultado, definir_acao, rotulo, label_capa))

    botao_filtrar_gravidade = tk.Button(opcoes_filtros_planetas, text="Filtrar por gravidade", bg="#37487B", fg="white", command=lambda:filtrar_gravidade(definir_acao, gerenciadorPlanetas, entrada, rotulo, resultado, label_capa))

    botao_filtrar_populacao = tk.Button(opcoes_filtros_planetas, text="Filtrar por população", bg="#37487B", fg="white", command=filtros_populacao)
    botao_populacao_intervalo = tk.Button(opcoes_populacao, text="Filtrar por intervalo", bg="#002699", fg="white", 
                                     command=lambda :buscar_intervalo(gerenciadorPersonagens, gerenciadorPlanetas, definir_acao, "populacao", rotulo, entrada, resultado, label_capa))
    botao_populacao_exato = tk.Button(opcoes_populacao, text="Filtrar por valor exato", bg="#002699", fg="white", 
                                 command=lambda : pesquisar_valor(gerenciadorPersonagens, gerenciadorPlanetas, "populacao", entrada, resultado, definir_acao, rotulo, label_capa))


    botao_planetas.pack(pady=5, fill="x", ipady=8)
    botao_buscar_nome_plan.pack(pady=4, fill="x")
    botao_buscar_prefixo_plan.pack(pady=4, fill="x")
    botao_filtrar_planetas.pack(pady=4, fill="x")
    botao_listar_todosPlanetas.pack(fill="x", pady=3)

    botao_filtrar_clima.pack(fill="x", pady=3)
    botao_clima_temperado.pack(fill="x", pady=3)
    botao_clima_arido.pack(fill="x", pady=3)
    botao_clima_tropical.pack(fill="x", pady=3)
    botao_clima_quente.pack(fill="x", pady=3)
    botao_clima_outros.pack(fill="x", pady=3)

    botao_filtrar_diametro.pack(fill="x", pady=3)
    botao_diametro_intervalo.pack(fill="x", pady=3) 
    botao_diametro_exato.pack(fill="x", pady=3)

    botao_filtrar_gravidade.pack(fill="x", pady=3)
    botao_filtrar_populacao.pack(fill="x", pady=3)
    botao_populacao_intervalo.pack(fill="x", pady=3) 
    botao_populacao_exato.pack(fill="x", pady=3)

    opcoes_missoes = tk.Frame(menu, bg="#252A38")
    
    def mostrar_missoes():
        if opcoes_missoes.winfo_ismapped(): 
            opcoes_missoes.pack_forget()
        else:
            opcoes_missoes.pack(fill="x", before=botao_sair) 
    
    botao_missoes = tk.Button(menu, text="Missões", bg="#001963", fg="white", command=mostrar_missoes)
    botao_viagem_mochila = tk.Button(opcoes_missoes, text="Viagem Espacial", bg="#343B50", fg="white", 
                                           command=lambda :viagem_mochila( gerenciadorPersonagens, entrada, resultado, rotulo, definir_acao, label_capa))

    botao_sair = tk.Button(menu, text="Sair", bg="#001963", fg="white", command = janela.destroy)
    
    botao_missoes.pack(pady=5, fill="x", ipady=8)
    botao_viagem_mochila.pack(pady = 4, fill="x")

    botao_sair.pack(pady=5, fill="x", ipady=8)

    #scrollbar
    scroll = tk.Scrollbar(painel)
    scroll.pack(side="right", fill="y")
    resultado.config(yscrollcommand=scroll.set) #atualiza a barra conforme o texto é percorrido
    scroll.config(command=resultado.yview) #faz a barra controlar a rolagem do texto

    return janela, entrada, resultado, botao_personagens, botao_planetas, botao_missoes, botao_sair