# 1- Conversor de Moeda
# Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

# * Valor em reais: R$ 100.00
# * Taxa do dólar: R$ 5.20
# * Taxa do euro: R$ 6.15
# O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
 
reais = 100.0
taxDolar = 5.2
taxEuro = 6.15

valorEmDolar = reais/taxDolar
valorEmEuro = reais/taxEuro

print(f'Valor: R$ {reais:.2f} \n'
    f'Convertido em dolar: US$ {valorEmDolar:.2f} \n'
    f'Convertido em euro: € {valorEmEuro:.2f}')