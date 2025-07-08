# 2 - Crie um script em Python que escreva dados em um arquivo CSV. O arquivo CSV deve conter informações de pessoas, com colunas:
# - Nome, Idade e Cidade.

import csv

dados = [
    ['ana', 24, 'SP'],
    ['joao', 31, 'RJ'],
    ['maria', 28, 'BH'],
]

cabecalho = ['Nome', 'Idade', 'Cidade']

arquivo = './arquivo.csv'

with open(arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(cabecalho)
    escritor.writerows(dados)

print(f"Dados escritos")