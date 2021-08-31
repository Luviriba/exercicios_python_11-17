# 16. Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade
# de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15
# por Km rodado.

km = float(input("Quantos quilometros foram percorridos com o carro?"))
dias = int(input("Por quantos dias o carro foi alugado?"))
preço_aluguel = dias * 60
preço_km = km * 0.15
preço_total = preço_aluguel + preço_km
print("você pagará R${} por ter alugado o carro por {} dias.".format(preço_aluguel, dias))
print("E pagará R${} por ter percorrido {} quilometros".format(preço_km, km))
print("Você pagará ao todo R${}".format(preço_total))