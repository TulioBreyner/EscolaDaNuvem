# Exercicio 1: Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais, possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória. ​

import random
import string

caracteres = string.ascii_letters + string.digits + '@#$%&!?'

try:
    tamanho = int(input("Quantos caracteres deve ter a senha? "))
    if tamanho < 4:
        print("A senha deve ter pelo menos 4 caracteres")
    else:
        senha = ''.join(random.choices(caracteres, k=tamanho))
        print(f"Senha gerada: {senha}")
except:
    print("Por favor, digite um número inteiro válido.")
