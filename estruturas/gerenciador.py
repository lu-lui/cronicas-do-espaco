#vai gerenciar as 3 estruturas para planetas e personagens
from estruturas.tabela_hash import TabelaHash
from estruturas.trie import Trie
from estruturas.arvoreB import ArvoreB

class Gerenciador():
    def __init__(self, tamanho):
        self.tabela_hash = TabelaHash(tamanho)
        self.trie = Trie()
        self.arvoreB = ArvoreB()

    def inserir(self, chave, registro):
        chave = " ".join(chave.lower().split())
        self.tabela_hash.inserir(chave, registro)
        self.trie.inserir(chave, registro)
       # self.arvoreB.inserir(chave, registro)

    def exibir_informacoes(self, titulo):
        print(titulo)
        print("Fator de carga:", round(self.tabela_hash.fator_de_carga() * 100, 2), "%")
        print("Número de colisões:", self.tabela_hash.colisoes)

    def buscar(self, chave):
        chave = " ".join(chave.lower().split())
        return self.tabela_hash.buscar(chave)

    def buscar_prefixo(self, prefixo):
        prefixo = " ".join(prefixo.lower().split())
        return self.trie.buscar(prefixo)

    def __iter__(self):
        return iter(self.tabela_hash)