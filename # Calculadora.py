# 1 Pede ao usuário que insira dois números inteiros
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

# 2. Realiza as quatro operações básicas
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
# Para divisão, verificamos se o segundo número não é zero
if num2 != 0:
    divisao = num1 / num2
else:
    divisao = "Não é possível dividir por zero."

# 3. Exibe os resultados de forma clara
print(f"\nResultados para os números {num1} e {num2}:")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")