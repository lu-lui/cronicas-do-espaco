from estruturas.tabela_hash import TabelaHash
from dados.swapi import carregar_planetas, carregar_personagens
from menu.menu import exibir_informacoes, menu

tabelaPlanetas = TabelaHash(89)
tabelaPersonagens = TabelaHash(127)

carregar_planetas(tabelaPlanetas)
carregar_personagens(tabelaPersonagens)

exibir_informacoes("Planetas__________________________________", tabelaPlanetas)
exibir_informacoes("Personagens__________________________________", tabelaPersonagens)

menu(tabelaPlanetas, tabelaPersonagens)