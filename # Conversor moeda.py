# 1. Cotação do dólar
cotacao_dolar = 5.25

# 2. Solicita ao usuário um valor em reais
valor_reais = float(input("Digite um valor em Reais (R$): "))

# 3. Converte para dólares
valor_dolares = valor_reais / cotacao_dolar

# 4. Exibe os resultados
print(f"Com a cotação do dólar a R$ {cotacao_dolar}")
print(f"O valor de R$ {valor_reais:.2f} equivale a US$ {valor_dolares:.4f}")