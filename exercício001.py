# """Faça um programa que calcule a media de um conjunto de números inseridos pelo usuário.
# O programa deve solicitar ao usuário que informe quantos números  deseja inserir; 
# Em um loop ,pedir ao usuário que insira cada número;
# Armazenar esses números em uma lista ;
# Calcular a média dos números e inserir o resultado.
# Dê um comando para para que o programa pare após a quantidade de numeros que foi digitada.

print("Olá, sou um programa Python que calcula a média de um conjunto de números.")

quantidade_de_numeros = int(input("Quantos números deseja inserir? "))

numeros = []
for i in range(quantidade_de_numeros):
  numero = float(input("Insira um número: "))
  numeros.append(numero)

media = sum(numeros) / len(numeros)

print("A média dos números é:", media)


while True:
  nova_entrada = input("Deseja inserir mais números? (S/N)")
  if nova_entrada == "S" :
    quantidade_de_numeros = int(input("Quantos números deseja inserir? "))
    numeros = []
    for i in range(quantidade_de_numeros):
      numero = float(input("Insira um número: "))
      numeros.append(numero)
    media = sum(numeros) / len(numeros)
    print("A média dos números é:", media)
  else:
    break
# Este programa primeiro solicita ao usuário que informe quantos números deseja inserir. Em seguida, ele cria um loop que itera pelo número especificado de vezes. 
# Em cada iteração, o programa pede ao usuário que insira um número e adiciona esse número à lista numeros. 
# Por fim, o programa calcula a média dos números e a imprime.

# O programa também oferece ao usuário a opção de inserir mais números. 
# Se o usuário escolher inserir mais números, o programa solicitará ao usuário quantos números deseja inserir e,
# em seguida, repetirá o processo de entrada e cálculo da média. 
# Se o usuário escolher não inserir mais números, o programa terminará.