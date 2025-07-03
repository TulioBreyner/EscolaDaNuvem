# Exercicio 2: Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'.
# O programa deve exibir o nome, email e país do usuário gerado.

import requests

def gerarUsuario():
    url = "https://randomuser.me/api/"
    
    try:
        resposta = requests.get(url)
        resposta.raise_for_status() 

        dados = resposta.json()
        usuario = dados['results'][0]

        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        print("==== Perfil de Usuário Aleatório ====")
        print(f"Nome : {nome}")
        print(f"E-mail : {email}")
        print(f"País : {pais}")
    except requests.RequestException as erro:
        print("Erro ao acessar a API:", erro)

gerarUsuario()
