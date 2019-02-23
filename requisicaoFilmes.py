import requests
import json


def pesquisarFilme(nomeFilme):
    try:
        req = requests.get("http://www.omdbapi.com/?apikey=[yourapikey&t=" + nomeFilme+"&type=movie")
        resposta = req.text
        if resposta.__contains__("Movie not found"):
            print ("Filme não encontrado, tente novamente")
        else:
            dicionario = json.loads(req.text)
            print("------", dicionario['Title'], "----------")
            print("Atores: ", dicionario['Actors'])
            print("Diretor: ", dicionario['Director'])
            print("Gênero:", dicionario['Genre'])
            print("Ano: ", dicionario['Year'])
            print("Nota do publico: ", dicionario['imdbRating'])
            print("Prêmios: ", dicionario['Awards'])
            print("Poster: ", dicionario['Poster'])
    except Exception as erro:
        print("Erro na requisição " + erro)


nomeFilme = input(
    "Digite o nome do filme que você deseja mais informações ou digite 'sair' para finalizar o programa: \n")
while nomeFilme != 'sair':
    pesquisarFilme(nomeFilme);
    nomeFilme = input(
        "\n Digite o nome do filme que você deseja mais informações ou digite 'sair' para finalizar o programa: \n")
