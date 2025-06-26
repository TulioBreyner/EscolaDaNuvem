# 2- Calculadora de Desconto
# Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

# * Nome do produto: "Camiseta"
# * Preço original: R$ 50.00
# * Porcentagem de desconto: 20%
# O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

nomeProduto = "Camiseta"
precoOriginal = 50.00
percentualDesconto = 20

valor_desconto = precoOriginal * (percentualDesconto /100)
preco_final = precoOriginal - valor_desconto

print(f"Produto: {nomeProduto} \n"
    f"Preço original: R$ {precoOriginal:.2f} \n"
    f"Desconto: {percentualDesconto}% \n"
    f"Valor do desconto: R$ {valor_desconto:.2f} \n"
    f"Preço com desconto: R$ {preco_final:.2f}")
