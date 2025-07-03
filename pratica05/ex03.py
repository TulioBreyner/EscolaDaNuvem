# Exercicio 3: Crie uma função que verifique se uma palavra ou frase é um palindromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda "Sim", se o resultado for False, responda "Não".

import unicodedata
import re

def palindromo(texto):
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

    texto_limpo = re.sub(r'[^a-zA-Z0-9]', '', texto).lower()
    
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"

entrada = input("Digite uma palavra: ")
print(palindromo(entrada))
