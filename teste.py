from estruturas.tabela_hash import TabelaHash
from modelos.planeta import Planeta

t = TabelaHash(89)
t.inserir("Tatooine", Planeta("Tatooine", "arid", "10465", "1 standard", "200000"))
t.inserir("Alderaan", Planeta("Alderaan", "temperate", "12500", "1 standard", "2000000000"))

print(t.qtd_elementos, t.colisoes, t.fator_de_carga())   # 2, 0 ou mais, ~0.0225
print(t.buscar("Tatooine"))
print(t.buscar("Inexistente"))                           # None
print([p.name for p in t.percorrer()])