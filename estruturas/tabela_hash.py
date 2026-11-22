from estruturas.interface import Estruturas

class TabelaHash(Estruturas):
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho
        self.colisoes = 0
        self.qtd_elementos = 0

    def funcao_hash(self, chave):
        soma = 0
        for caractere in chave:
            soma += ord(caractere)
        return soma % self.tamanho

    def inserir(self, chave, registro):
        posicao = self.funcao_hash(chave)
        #depois de achar a posição se houver colisão vamos fazer a sondagem quadrática
        #fórmula da sondagem quadrática (h + i^2) % tamanho
        #h nossa posição inicialmente calculada e i o número de tentativas 
        #que fizemos de achar um lugar vazio

        i = 0
        while self.tabela[(posicao + i ** 2) % self.tamanho] is not None:
            self.colisoes += 1
            i += 1

        nova_posicao = (posicao + i ** 2) % self.tamanho
        self.tabela[nova_posicao] = (chave, registro)
        self.qtd_elementos += 1

    def buscar(self, chave):
        soma = 0
        i = 0

        for caractere in chave:
            soma += ord(caractere)
        posicaoInicial = soma % self.tamanho
        posicao = posicaoInicial

        while self.tabela[posicao] is not None and self.tabela[posicao][0] != chave and i < self.tamanho:
            i += 1
            posicao = (posicaoInicial + i ** 2) % self.tamanho

        if i == self.tamanho or self.tabela[posicao] is None:
            return None
        else:
            return self.tabela[posicao][1]

    def fator_de_carga(self):
        return self.qtd_elementos / self.tamanho

    def percorrer(self):
        elementos = []
        for elemento in self.tabela:
            if elemento is not None:
                elementos.append(elemento[1])
        return elementos
