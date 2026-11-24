#vai gerenciar as 4 estruturas para planetas 
from estruturas.tabela_hash import TabelaHash
from estruturas.trie import Trie
from estruturas.arvoreB import ArvoreB

class GerenciadorPlaneta():
    def __init__(self, tamanho):
        self.tabela_hash = TabelaHash(tamanho)
        self.trie = Trie()
        self.arvoreB_diametro = ArvoreB()
        self.arvoreB_populacao = ArvoreB()

    def inserir(self, chave, registro):
        chave = " ".join(chave.lower().split())
        self.tabela_hash.inserir(chave, registro)
        self.trie.inserir(chave, registro)

        diametro = self.arrumar_numero(registro.diameter)
        if diametro is not None:
            self.arvoreB_diametro.inserir(diametro, registro)
        populacao = self.arrumar_numero(registro.population)
        if populacao is not None:
            self.arvoreB_populacao.inserir(populacao, registro)

    def arrumar_numero(self, numero):
        numero = str(numero).replace(",", "").strip()

        if numero.lower() in ["unknown", ""]:
            return None
        else:
            return float(numero)

    def exibir_informacoes(self):
        return f"Fator de carga: {round(self.tabela_hash.fator_de_carga() * 100, 2)} %\nNúmero de colisões: {self.tabela_hash.colisoes}"

    def buscar_nome(self, chave):
        chave = " ".join(chave.lower().split())
        return self.tabela_hash.buscar(chave)

    def buscar_prefixo(self, prefixo):
        prefixo = " ".join(prefixo.lower().split())
        return self.trie.buscar(prefixo)

    def buscar_intervalo_diametro(self, inicio, fim):
        return self.arvoreB_diametro.buscar_intervalo(inicio, fim)

    def buscar_diametro(self, valor):
        return self.arvoreB_diametro.buscar(valor)

    def buscar_intervalo_populacao(self, inicio, fim):
        return self.arvoreB_populacao.buscar_intervalo(inicio, fim)

    def buscar_populacao(self, valor):
        return self.arvoreB_populacao.buscar(valor)

    def __iter__(self):
        return iter(self.tabela_hash)