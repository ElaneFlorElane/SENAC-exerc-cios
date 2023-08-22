"""Desenvolva um programa que simula um sistema de cadastro de produtos. 
O programa deve:
Utilizar um dicionário para armazenar informações sobre os produtos, como nome, preço e quantidade em estoque.
Oferecer um menu com as opções: cadastrar novo produto, verificar estoque de um produto e sair.
Utilizar estruturas de condição para executar as ações escolhidas pelo usuário.
Utilizar estruturas de repetição para permitir que o usuário realize múltiplas operações."""

produtos = {}

while True:
  print("Menu:")
  print("1. Cadastrar novo produto")
  print("2. Verificar estoque de um produto")
  print("3. Sair")

  opcao = int(input("Digite sua escolha: "))

  if opcao == 1:
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade em estoque do produto: "))

    produtos[nome] = {"preco": preco, "quantidade": quantidade}

  elif opcao == 2:
    nome = input("Digite o nome do produto: ")

    if nome in produtos:
      print("O produto", nome, "tem", produtos[nome]["quantidade"], "unidades em estoque.")
    else:
      print("O produto", nome, "não está cadastrado.")

  elif opcao == 3:
    break

print("Obrigado por usar o sistema de cadastro de produtos!")
