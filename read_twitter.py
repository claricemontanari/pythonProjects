from twitter import Twitter
import urllib.parse

# keys geradas pelo próprio twitter  atraves de https://developer.twitter.com/en/apps/
consumer_key = '...'
consumer_secret = '...'

token_key = '...'
token_secret = '...'

twitter = Twitter(consumer_key, consumer_secret, token_key, token_secret)

pesquisa = input("Digite o que deseja pesquisar no Twitter: \n")
# biblioteca para tratar o input e retirar caracteres especiais
pesquisa_codificada = urllib.parse.quote(pesquisa, safe='')
pesquisa = twitter.search(pesquisa_codificada)
