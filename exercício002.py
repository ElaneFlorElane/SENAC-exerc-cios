# Crie um programa que solicita ao usuário que insira uma lista de números inteiros. 
# O programa deve:
# Receber uma lista de números inteiros separados por espaço.
# Armazenar esses números em uma lista.
# Utilizar uma estrutura de repetição para percorrer a lista e verificar se cada número é par ou ímpar.
# Exibir quantos números pares e quantos números ímpares foram inseridos.

numeros = input("Insira uma lista de números inteiros separados por espaço: ")

numeros_list = numeros.split()

pares = 0
impares = 0

for numero in numeros_list:
  if int(numero) % 2 == 0:
    pares += 1
  else:
    impares += 1

print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)


