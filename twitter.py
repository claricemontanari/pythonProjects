import oauth2
import json

class Twitter:

    # keys geradas pelo próprio twitter  atraves de https://developer.twitter.com/en/apps/
    def __init__(self, consumer_key, consumer_secret, token_key, token_secret):
        self.connection(consumer_key, consumer_secret, token_key, token_secret)

    def connection(self, consumer_key, consumer_secret, token_key, token_secret):
        # metodos para autenticação oauth no twitter
        self.consumer = oauth2.Consumer(consumer_key, consumer_secret)
        self.token = oauth2.Token(token_key, token_secret)
        self.cliente = oauth2.Client(self.consumer, self.token)

    def search(self, word):

        # faz a pesquisa no twitter de acordo com o termo após o q
        # para mais informações : https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets
        requisicao = self.cliente.request(
            "https://api.twitter.com/1.1/search/tweets.json?q=" + word)  # requisicao é uma tuple

        # Conversão em string o indice 1 da tupla retornada pelo request, pois ele é retornado em byte
        decodificado = requisicao[1].decode()
        # Conversão em json para facilitar leitura
        objeto_json = json.loads(decodificado)

        # biblioteca utilizada para imprimir o json de forma legivel
        # pprint.pprint(objeto_json['statuses'])

        # a tag statuses é a tag com as informações desejadas
        # for é utilizado para mostrar cada texto de twitt separadamente
        for twitt in objeto_json['statuses']:
            print("user: ", twitt['user']['screen_name'])
            print("text: ", twitt['text'])
            print(" -------------------------- ")




