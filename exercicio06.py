print('''
Especificação        |      Preço Unitário
100 Cachorro quente  |            1,10
101 Bauru simples    |            1,30
102 Bauru c/ovo      |            1,50
103 Hamburger        |            1,10
104 Cheeseburger     |            1,30
105 Refrigerante     |            1,00
      ''')

cod = input("Digite o código:")
quant = int(input("Digite o quantitativo:"))

if cod == "100":
    precoTotal = quant * 1.1
elif cod == "101":
    precoTotal = quant * 1.3
elif cod == "102":
    precoTotal = quant * 1.5
elif cod == "103":
    precoTotal = quant * 1.1
elif cod == "104":
    precoTotal = quant * 1.3
elif cod == "105":
    precoTotal = quant * 1.0
else:
    print("Digite um código válido")

print("Seu lanche vai custar", precoTotal)


