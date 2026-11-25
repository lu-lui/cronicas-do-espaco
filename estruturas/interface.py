#import do método abstrato
from abc import ABC, abstractmethod

class Estruturas( ABC ): #contrato com as estruturas de dados
    @abstractmethod
    def inserir( self, chave, registro ):
        pass

    @abstractmethod
    #busca algo em específico
    def buscar( self, chave ):
        pass