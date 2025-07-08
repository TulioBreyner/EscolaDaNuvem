# 4 -  Crie um script em Python que leia e escreva dados em um arquivo JSON. O arquivo JSON deve conter informações de uma pessoa, com campos:
# - Nome, Idade e Cidade.

import json

pessoa_dados = {
    "nome": "Ana",
    "idade": 30,
    "cidade": "Curitiba"
}

arquivo = 'pessoa.json'

try:
    with open(arquivo, 'w', encoding='utf-8') as arquivo_aberto:
        json.dump(pessoa_dados, arquivo_aberto, ensure_ascii=False, indent=4)
    
    print("Escrita concluída \n")
except Exception as e:
    print(f"Erro ao escrever o arquivo: {e}")

try:
    with open(arquivo, 'r', encoding='utf-8') as arquivo_aberto:
        dados_lidos = json.load(arquivo_aberto)
        
        print("Dados lidos:")
        print(f"Nome: {dados_lidos['nome']}")
        print(f"Idade: {dados_lidos['idade']}")
        print(f"Cidade: {dados_lidos['cidade']}")
except FileNotFoundError:
    print(f"arquivo não encontrado.")
except Exception as e:
    print(f"Erro: {e}")