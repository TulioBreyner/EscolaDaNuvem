# 3 - Crie um script em Python que leia um arquivo CSV e exiba os dados na tela. O arquivo CSV deve conter informações de pessoas, com colunas:
# - Nome, Idade e Cidade.

import csv

arquivo = 'arquivo.csv'

try:
    with open(arquivo, 'r', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        
        cabecalho = next(leitor_csv)
        print(f"Cabeçalho: {cabecalho}")
        for linha in leitor_csv:
            print(f"Nome: {linha[0]}, Idade: {linha[1]}, Cidade: {linha[2]}")

except FileNotFoundError:
    print(f"arquivo não encontrado")
except Exception as e:
    print(f"erro: {e}")