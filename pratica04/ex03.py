# Exercicio 3: Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP.
# O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.

import requests

cep = input("Informe o CEP: ")
url = f"https://viacep.com.br/ws/{cep}/json/"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()

    dados = resposta.json()

    logradouro = dados["logradouro"]
    bairro = dados["bairro"]
    cidade = dados["localidade"]
    estado = dados["estado"]

    print(f"Logradouro: {logradouro}\n"
            f"Bairro: {bairro}\n"
            f"Cidade: {cidade}\n"
            f"Estado: {estado}")

except requests.RequestException as erro:
    print("Erro ao acessar a API:", erro)

