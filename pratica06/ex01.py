# 1 - Desenvolva uma calculadora em Python que realize as quatro operações básicas (adição, subtração, multiplicação e divisão) entre dois números. A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operação. Siga as especificações abaixo:

# A calculadora deve solicitar ao usuário que insira dois números e uma operação.
# As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).
# O programa deve continuar solicitando entradas até que uma operação válida seja concluída.
# Trate os seguintes erros:
# Entrada inválida (não numérica) para os números
# Divisão por zero
# Operação inválida
# Use try/except para capturar e tratar os erros apropriadamente.
# Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.
# Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa

def calcular():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
        except ValueError:
            print("Erro: entrada inválida. Por favor, digite um número válido.")
            continue

        try:
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: entrada inválida. Por favor, digite um número válido.")
            continue

        operacao = input("Digite a operação (+, -, *, /): ")

        try:
            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Divisão por zero não é permitida.")
                resultado = num1 / num2

            print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
            break 

        except ZeroDivisionError as e:
            print(f"Erro: {e}")
            continue

calcular()
