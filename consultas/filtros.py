def ler_intervalo():
    while True:
        try:
            minimo = int( input( "Valor mínimo: " ) )
            maximo = int( input( "Valor máximo: " ) )
        except ValueError:
            print( "Digite apenas numeros inteiros" )
            continue
        
        if minimo <= maximo:
            return minimo, maximo
        print( "O mínimo não pode ser maior que o máximo." )

def filtrarPlanetas(tabelaPlanetas):
    while True:
        print( "\nSelecione uma opção: " )
        print( "1 - Listar todos" )
        print( "2 - Filtrar por clima" )
        print( "3 - Filtrar por diâmetro" )
        print( "4 - Filtrar por gravidade" )
        print( "5 - Filtrar por população" )
        print( "0 - Voltar" )
        opcao = input( "Escolha: " )
                
        while opcao != "0" and opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4" and opcao != "5":
            opcao = input( "Opção inválida! Tente novamente:" )

        match opcao:
            case "0":
                return
            case "1":
                flag = False
                for planeta in tabelaPlanetas.percorrer():
                    if planeta is not None:
                        print( "\nName: ", planeta.name )
                        print( "Climate: ", planeta.climate )
                        print( "Diameter: ", planeta.diameter )
                        print( "Gravity: ", planeta.gravity )
                        print( "Population: ", planeta.population )
                        flag = True
                if not flag:                      
                    print( "Nenhum resultado encontrado." )
            case "2":
                print( "\n---Clima---" )
                print( "Selecione o clima desejado:" )
                opcao = input( "1. Temperado \n2. Arido \n3. Tropical \n4. Quente \n5. Outros\n" )

                while opcao not in [ "1", "2", "3", "4", "5" ]:
                    print( "Opção inválida! \nSelecione um clima:" )
                    opcao = input( "1. Temperado \n2. Arido \n3. Tropical \n4. Quente \n5. Outros\n" )

                flag = False #flag que liga quando acha a informação  
                match opcao:
                    case "1":
                        for planeta in tabelaPlanetas.percorrer(): #os planetas tem mais de uma caracteristica climática
                            if planeta is not None:    #verifica se a temperatura selecionada está etre elas
                                if "temperate" in planeta.climate: 
                                    print( "\nName: ", planeta.name )
                                    print( "Climate: ", planeta.climate )
                                    flag = True
                    case "2":
                        for planeta in tabelaPlanetas.percorrer():
                            if planeta is not None:
                                if "arid" in planeta.climate:
                                    print( "\nName: ", planeta.name )
                                    print( "Climate: ", planeta.climate )
                                    flag = True            
                    case "3":
                        for planeta in tabelaPlanetas.percorrer():
                            if planeta is not None:
                                if "tropical" in planeta.climate:
                                    print( "\nName: ", planeta.name )
                                    print( "Climate: ", planeta.climate )
                                    flag = True
                    case "4":
                        for planeta in tabelaPlanetas.percorrer():
                            if planeta is not None:
                                if "hot" in planeta.climate:
                                    print( "\nName: ", planeta.name )
                                    print( "Climate: ", planeta.climate )
                                    flag = True
                    case "5":
                        for planeta in tabelaPlanetas.percorrer():
                            if planeta is not None:
                                if "temperate" not in planeta.climate and "arid" not in planeta.climate and "tropical" not in planeta.climate and "hot" not in planeta.climate:
                                    print( "\nName: ", planeta.name )
                                    print( "Climate: ", planeta.climate )
                                    flag = True
                if not flag:                      
                    print( "Nenhum resultado encontrado." )
            case "3":
                print( "\n---Diâmetro---" )
                print( "Digite o intervalo de diâmetro:" )
                minimo, maximo = ler_intervalo()

                flag = False
                for planeta in tabelaPlanetas.percorrer():
                    if planeta is not None:
                        if planeta.diameter != "unknown":
                            if minimo <= int( planeta.diameter ) <= maximo:
                                print( "\nName: ", planeta.name )
                                print( "Diameter: ", planeta.diameter )
                                flag = True
                if not flag:                      
                    print( "Nenhum resultado encontrado." )
                        
            case "4":
                print( "\n---Gravidade---" )
                gravidade = input( "Digite a gravidade exata (ex: 1 standard): " )

                flag = False
                for planeta in tabelaPlanetas.percorrer():
                    if planeta is not None:
                        if planeta.gravity == gravidade:
                            print( "\nName: ", planeta.name )
                            print( "Gravity: ", planeta.gravity )
                            flag = True
                if not flag:                      
                    print( "Nenhum resultado encontrado." )
            case "5":
                print( "\n---População---" )
                print( "Digite o intervalo de população:" )
                minimo, maximo = ler_intervalo()

                flag = False
                for planeta in tabelaPlanetas.percorrer():
                    if planeta is not None:
                        if planeta.population != "unknown":
                            if minimo <= int( planeta.population ) <= maximo:
                                print( "\nName: ", planeta.name )
                                print( "Population: ", planeta.population )
                                flag = True
                if not flag:                      
                    print( "Nenhum resultado encontrado." )          

def filtrarPersonagens(tabelaPersonagens):
    while True:
        print( "\nSelecione uma opção: " )
        print( "1 - Listar todos" )
        print( "2 - Filtrar por peso" )
        print( "3 - Filtrar por altura" )
        print( "4 - Filtrar por gênero" )
        print( "5 - Filtrar por cor dos olhos" )
        print( "6 - Filtrar por planeta" )
        print( "0 - Voltar" )
        opcao = input( "Escolha: " )
        
        while opcao != "0" and opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4" and opcao != "5" and opcao != "6":
            opcao = input( "Opção inválida! Tente novamente:" )

        match opcao:
            case "0":
                return
            case "1":
                flag = False
                for personagem in tabelaPersonagens.percorrer():
                    if personagem is not None:
                        print( "\nName: ", personagem.name )
                        print( "Mass: ", personagem.mass )
                        print( "Height: ", personagem.height )
                        print( "Gender: ", personagem.gender )
                        print( "Eye Color: ", personagem.eye_color )
                        flag = True
                if not flag:                      
                    print( "Nenhum resultado encontrado." )
            case "2":
                print( "\n---Peso---" )
                print( "Digite o intervalo de peso:" )
                minimo, maximo = ler_intervalo()

                flag = False
                for personagem in tabelaPersonagens.percorrer():
                    if personagem is not None:
                        if personagem.mass != "unknown":
                            if minimo <= float( personagem.mass.replace( "," , "" ) ) <= maximo:
                                print( "\nName: ", personagem.name )
                                print( "Mass: ", personagem.mass ) 
                                flag = True
                if not flag:                      
                    print( "Nenhum resultado encontrado." )                  
            case "3":
                print( "\n---Altura---" )
                print( "Digite o intervalo de altura:" )
                minimo, maximo = ler_intervalo()

                flag = False
                for personagem in tabelaPersonagens.percorrer():
                    if personagem is not None:
                        if personagem.height != "unknown":
                            if minimo <= int( personagem.height ) <= maximo:
                                print( "\nName: ", personagem.name )
                                print( "Height: ", personagem.height ) 
                                flag = True
                if not flag:                      
                    print( "Nenhum resultado encontrado." )              
            case "4":
                print( "\n---Gênero---" )
                print( "Selecione o gênero:" )
                opcao = input( "1. Feminino \n2. Masculino\n" )

                while opcao != "1" and opcao != "2":
                    print( "Opção inválida! \nSelecione um gênero:" )
                    opcao = input( "1. Feminino \n2. Masculino\n" )   
                
                if opcao == "1":
                    flag = False
                    for personagem in tabelaPersonagens.percorrer():
                        if personagem is not None:
                            if( personagem.gender == "female" ):
                                print( "\nName: ", personagem.name )
                                print( "Gender: ", personagem.gender )
                                flag = True
                    if not flag:                      
                        print( "Nenhum resultado encontrado." )
                elif opcao == "2":
                    flag = False
                    for personagem in tabelaPersonagens.percorrer():
                        if personagem is not None:
                            if( personagem.gender == "male" ):
                                print( "\nName: ", personagem.name )
                                print( "Gender: ", personagem.gender )
                                flag = True
                    if not flag:                      
                        print( "Nenhum resultado encontrado." ) 
            case "5":
                print( "\n---Cor dos olhos---" )
                print( "Selecione a cor desejada:" )
                opcao = input( "1. Preto \n2. Castanho \n3. Azul \n4. Amarelo \n5. Colorido\n" )

                while opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4" and opcao != "5":
                    print( "Opção inválida! \nSelecione uma cor de olhos:" )
                    opcao = input( "1. Preto \n2. Castanho \n3. Azul \n4. Amarelo \n5. Colorido\n" )

                flag = False  
                match opcao:
                    case "1":
                        for personagem in tabelaPersonagens.percorrer():
                            if personagem is not None:
                                if( personagem.eye_color == "black" ):
                                    print( "\nName: ", personagem.name )
                                    print( "Eye Color: ", personagem.eye_color )
                                    flag = True
                    case "2":
                        for personagem in tabelaPersonagens.percorrer():
                            if personagem is not None:
                                if( personagem.eye_color == "brown" or personagem.eye_color == "hazel" ):
                                    print( "\nName: ", personagem.name )
                                    print( "Eye Color: ", personagem.eye_color )
                                    flag = True
                    case "3":
                        for personagem in tabelaPersonagens.percorrer():
                            if personagem is not None:
                                if( personagem.eye_color == "blue" ):
                                    print( "\nName: ", personagem.name )
                                    print( "Eye Color: ", personagem.eye_color )
                                    flag = True
                    case "4":
                        for personagem in tabelaPersonagens.percorrer():
                            if personagem is not None:
                                if( personagem.eye_color == "yellow" ):
                                    print( "\nName: ", personagem.name )
                                    print( "Eye Color: ", personagem.eye_color )
                                    flag = True
                    case "5":
                        for personagem in tabelaPersonagens.percorrer():
                            if personagem is not None:
                                if personagem.eye_color not in [ "black", "brown", "hazel", "blue", "yellow", "" ]:
                                    print( "\nName: ", personagem.name )
                                    print( "Eye Color: ", personagem.eye_color )
                                    flag = True
                if not flag:                      
                    print( "Nenhum resultado encontrado." )
            case "6":
                flag = False
                p = input( "Digite o planeta: \n" )
                for personagem in tabelaPersonagens.percorrer():
                    if personagem is not None:
                        if( personagem.homeworld == p ):
                            print( "\nName: ", personagem.name )
                            print( "Homeworld: ", personagem.homeworld )
                            print( "Massa: ", personagem.mass )
                            flag = True
                if not flag:                      
                    print( "Nenhum resultado encontrado." ) 
