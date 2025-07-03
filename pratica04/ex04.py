# Exercicio 4: Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, máximo e mínimo da cotação, além da data e hora da última atualização.
# Utilize a API da AwesomeAPI para obter os dados de cotação.​

import requests

moeda = input("Informe a moeda: ").upper()
url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()

    dados = resposta.json()
    
    chave = moeda + "BRL"

    cotacao = dados[chave]
    valorAtual = cotacao["bid"]
    valorMax = cotacao["high"]
    valorMin = cotacao["low"]
    dataHora = cotacao["create_date"]

    print(f"\nCotação de {moeda} em relação ao BRL:")
    print(f"Valor atual: R$ {valorAtual}")
    print(f"Valor máximo: R$ {valorMax}")
    print(f"Valor mínimo: R$ {valorMin}")
    print(f"Data e hora da última atualização: {dataHora}")

except requests.RequestException as erro:
    print("Erro ao acessar a API:", erro)
