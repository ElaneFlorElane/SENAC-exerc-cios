""". A função is_prime() primeiro verifica se o
número é menor ou igual a 1. Se for, 
a função retorna False. Caso contrário, 
a função usa uma estrutura de repetição para verificar 
se o número é divisível por algum outro número. 
Se o número for divisível por qualquer outro número, 
a função retorna False. Se o número não for divisível por 
nenhum outro número, a função retorna True. 
O programa principal, em seguida, usa a função is_prime() 
para verificar se o número inserido pelo usuário é primo. 
Se o número for primo, o programa imprime "O número é primo". 
Se o número não for primo, o programa imprime
 "O número não é primo"."""

# Crie um programa que verifica se um número inteiro inserido pelo usuário é primo. O programa deve:
# Solicitar ao usuário que insira um número inteiro.
# Utilizar uma estrutura de repetição para verificar se o número é divisível por algum outro número além de 1 e ele mesmo.
# Exibir se o número é primo ou não.

def is_prime(numero):
  if numero <= 1:
    return False
  for i in range(2, numero):
    if numero % i == 0:
      return False
  return True

numero = int(input("Insira um número inteiro: "))

if is_prime(numero):
  print("O número é primo.")
else:
  print("O número não é primo.")
