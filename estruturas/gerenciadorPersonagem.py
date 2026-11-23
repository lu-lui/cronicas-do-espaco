#vai gerenciar as 4 estruturas para personagens
from estruturas.tabela_hash import TabelaHash
from estruturas.trie import Trie
from estruturas.arvoreB import ArvoreB

class GerenciadorPersonagem():
    def __init__(self, tamanho):
        self.tabela_hash = TabelaHash(tamanho)
        self.trie = Trie()
        self.arvoreB_altura = ArvoreB()
        self.arvoreB_peso = ArvoreB()

    def inserir(self, chave, registro):
        chave = " ".join(chave.lower().split())
        self.tabela_hash.inserir(chave, registro)
        self.trie.inserir(chave, registro)

        peso = self.arrumar_numero(registro.mass)
        if peso is not None:
            self.arvoreB_peso.inserir(peso, registro)
        altura = self.arrumar_numero(registro.height)
        if altura is not None:
            self.arvoreB_altura.inserir(altura, registro)

    def arrumar_numero(self, numero):
        numero = str(numero).replace(",", "").strip()

        if numero.lower() in ["unknown", ""]:
            return None
        else:
            return float(numero)

    def exibir_informacoes(self, titulo):
        print(titulo)
        print("Fator de carga:", round(self.tabela_hash.fator_de_carga() * 100, 2), "%")
        print("Número de colisões:", self.tabela_hash.colisoes)

    def buscar_nome(self, chave):
        chave = " ".join(chave.lower().split())
        return self.tabela_hash.buscar(chave)

    def buscar_prefixo(self, prefixo):
        prefixo = " ".join(prefixo.lower().split())
        return self.trie.buscar(prefixo)

    def buscar_intervalo_altura(self, inicio, fim):
        return self.arvoreB_altura.buscar_intervalo(inicio, fim)

    def buscar_altura(self, valor):
        return self.arvoreB_altura.buscar(valor)

    def buscar_intervalo_peso(self, inicio, fim):
        return self.arvoreB_peso.buscar_intervalo(inicio, fim)

    def buscar_peso(self, valor):
        return self.arvoreB_peso.buscar(valor)

    def __iter__(self):
        return iter(self.tabela_hash)