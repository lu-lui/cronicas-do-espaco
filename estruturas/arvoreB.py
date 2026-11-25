from estruturas.interface import Estruturas

class NoArvoreB():
    def __init__( self ):
        self.filhos = []
        self.chaves = []
        self.registros = []
        self.folha = True

class ArvoreB( Estruturas ):
    def __init__( self ):
        self.M = 4
        self.raiz = NoArvoreB()

    def inserir( self, chave, registro ):
        no = self.raiz 
        caminho = []

        while True:
            i = 0

            #ENCONTRAR A POSIÇÃO NA CHAVE
            #inserir a chave na posição correta no nó
            #Ex:[20, 30, 60] queremos inserir 50 -> vai entre 30 e 60
            while i < len( no.chaves ) and no.chaves[ i ] < chave:
                        i += 1

            #VERIFICAR SE A CHAVE JÁ EXISTE
            #se nn chegou no indice dps da última chave e a 
            #chave está na lista só coloca o registro
            if i < len( no.chaves ) and chave == no.chaves[ i ]:
                no.registros[ i ].append( registro )
                break
            else:
                #SE FOR FOLHA, INSERIR E PARAR
                if no.folha:
                    no.chaves.insert( i, chave )
                    no.registros.insert( i, [ registro ] )

                    if len( no.chaves ) >= self.M:
                         self.dividir_no( no, caminho )
                    break
                else:
                #SE NÃO É FOLHA, DESCER PRO FILHO CERTO
                    caminho.append( no )
                    no = no.filhos[ i ]

    def dividir_no( self, no, caminho ):
        indiceMediana = ( len( no.chaves ) // 2 ) - 1
        noEsquerda = NoArvoreB()
        noDireita = NoArvoreB()

        chaveMediana = no.chaves[ indiceMediana ]
        registrosMediana = no.registros[ indiceMediana ]

        noEsquerda.chaves = no.chaves[ :indiceMediana ]
        noEsquerda.registros = no.registros[ :indiceMediana ]
        noEsquerda.filhos = no.filhos[ :indiceMediana + 1 ]
        noEsquerda.folha = no.folha

        noDireita.chaves = no.chaves[ indiceMediana + 1: ]
        noDireita.registros = no.registros[ indiceMediana + 1: ]
        noDireita.filhos = no.filhos[ indiceMediana + 1: ]
        noDireita.folha = no.folha

        if caminho:
            no_pai = caminho.pop()
            i = 0
            while i < len( no_pai.chaves ) and no_pai.chaves[ i ] < chaveMediana:
                i += 1

            no_pai.chaves.insert( i, chaveMediana )
            no_pai.registros.insert( i, registrosMediana )

            j = 0
            for filho in no_pai.filhos:
                if filho is no:
                    break
                j += 1

            no_pai.filhos.pop( j )
            no_pai.filhos.insert( j, noEsquerda )
            no_pai.filhos.insert( j + 1, noDireita )

            if len( no_pai.chaves ) >= self.M:
                 self.dividir_no( no_pai, caminho )

        else:
            nova_raiz = NoArvoreB()
            nova_raiz.chaves.insert( 0, chaveMediana )
            nova_raiz.registros.insert( 0, registrosMediana )
            nova_raiz.filhos.insert( 0, noEsquerda )
            nova_raiz.filhos.insert( 1, noDireita )
            nova_raiz.folha = False
            self.raiz = nova_raiz

    def buscar( self, chave ):
        no = self.raiz

        while True:
            i = 0
            while i < len( no.chaves ) and no.chaves[ i ] < chave:
                i += 1
            
            if i < len( no.chaves ) and chave == no.chaves[ i ]:
                return no.registros[ i ]
            else:
                #se for folha retorna None
                if no.folha:
                    return None
                else:
                    #se nn é folha desce pro filho
                    no = no.filhos[ i ]

    def buscar_intervalo( self, inicio, fim ):
        resultado = []
        self.buscar_intervalo_aux( self.raiz, inicio, fim, resultado )
        return resultado

    def buscar_intervalo_aux( self, no, inicio, fim, resultado ):
        for i in range( len( no.chaves ) ):
            #se o nó nn é folha procura o intervalo tbm nos filhos
            if not no.folha:
                self.buscar_intervalo_aux( no.filhos[ i ], inicio, fim, resultado )

            if inicio <= no.chaves[ i ] <= fim:
                resultado.extend( no.registros[ i ] )

        if not no.folha:
            self.buscar_intervalo_aux( no.filhos[ -1 ], inicio, fim, resultado )    