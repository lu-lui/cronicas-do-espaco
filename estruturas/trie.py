from estruturas.interface import Estruturas

class NoTrie():
    def __init__(self):
        self.filhos = {}    #filhos de cada nó
        self.fim_da_palavra = False
        self.registro = None

class Trie(Estruturas):
    def __init__(self):
        self.raiz = NoTrie()

    def inserir(self, chave, registro):
        chave = chave.lower()
        no = self.raiz  #começa a inserção na raiz

        for caractere in chave:
            if caractere not in no.filhos:  #se o caractere nn ta nos filhos do nó atual insere ele
                no.filhos[caractere] = NoTrie()

            no = no.filhos[caractere]   #avança pro nó correspondente a o caractere atual p ver o próximo

        #terminou o nome - marca fim de palavra e guarda o objeto/registro
        no.fim_da_palavra = True
        no.registro = registro

    def buscar(self, chave):
        chave = chave.lower()
        no = self.raiz

        for caractere in chave: #acha o prefixo
            if caractere not in no.filhos:
                return []

            no = no.filhos[caractere]

        resultados = []
        self.percorrer(no, resultados) #vai receber os registros de tudo que tiver o prefixo buscado

        return resultados

    #vai percorrer os filhos do nó passado procurando tudo que vem dps de certo prefixo
    #dfs - recursivo
    def percorrer(self, no, resultados):
        if no.fim_da_palavra:
            resultados.append(no.registro)

        for filho in no.filhos.values():
            self.percorrer(filho, resultados)

    def __iter__(self):
        resultados = []
        self.percorrer(self.raiz, resultados)
        yield from resultados