# Exercicio 2: Crie uma função que calcule a idade de uma pessoa em dias, baseado no ano de nascimento.from datetime import date

from datetime import date

def calcular_idade_em_dias(ano_nascimento):
    ano_atual = date.today().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365 
    return idade_dias

nascimento = int(input("Informe o ano que nasceu: "))
print(calcular_idade_em_dias(nascimento))  