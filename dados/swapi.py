import requests #se der erro colocar no terminal "pip install requests"

from modelos.planeta import Planeta
from modelos.personagem import Personagem

def carregar_planetas(tabela):
    planetasLink = "https://swapi.dev/api/planets/"

    while planetasLink is not None:
        planetasRespostas = requests.get(planetasLink)
        planetasDados = planetasRespostas.json()

        for planeta in planetasDados["results"]:
            #só os dados que queremos de cada planeta - parsing
            novo_planeta = Planeta(
                planeta["name"],
                planeta["climate"],
                planeta["diameter"],
                planeta["gravity"],
                planeta["population"]
            )
            tabela.inserir(planeta["name"], novo_planeta)

        planetasLink = planetasDados["next"]

def carregar_personagens(tabela):
    PersonagemLink = "https://swapi.dev/api/people/"

    while PersonagemLink is not None:
        PersonagemRespostas = requests.get(PersonagemLink)
        PersonagemDados = PersonagemRespostas.json()

        for personagem in PersonagemDados["results"]:
            #na API homeworld é um lin, então pegamos o nome do planeta
            linkHomeworld = personagem["homeworld"]
            respostaHomeworld = requests.get(linkHomeworld)
            dadosHomeworld = respostaHomeworld.json()
            nomeHomeworld = dadosHomeworld["name"]

            nova_personagem = Personagem(
                personagem["name"],
                personagem["mass"],
                personagem["height"],
                personagem["gender"],
                personagem["eye_color"],
                nomeHomeworld
            )
            tabela.inserir(personagem["name"], nova_personagem)

        PersonagemLink = PersonagemDados["next"]
