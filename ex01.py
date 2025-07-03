# Exercicio 1: Crie uma  função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de gorjeta desejada.
# Calcula o valor da gorjeta baseada no total a conta e na porcentagem desejada.

def calcular_gorjeta(valor, taxa):
    percent = taxa/100
    gorjeta =  valor*percent
    return gorjeta

conta = float(input("Valor da conta: "))
taxa = int(input("Quantos % de gorjeta? "))

print(f'Gorjeta = R${calcular_gorjeta(conta, taxa):.2f}')