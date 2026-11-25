from estruturas.gerenciadorPersonagem import GerenciadorPersonagem
from estruturas.gerenciadorPlaneta import GerenciadorPlaneta
from dados.swapi import carregar_planetas, carregar_personagens
from interface.janela_principal import criar_janela

gerenciadorPlanetas = GerenciadorPlaneta( 89 )
gerenciadorPersonagens = GerenciadorPersonagem( 127 )

carregar_planetas( gerenciadorPlanetas )
carregar_personagens( gerenciadorPersonagens )

#criar a interface
janela, entrada, resultado, botao_personagens, botao_planetas, botao_missoes, botao_sair = criar_janela( gerenciadorPersonagens, gerenciadorPlanetas )

#iniciar a interface
janela.mainloop()