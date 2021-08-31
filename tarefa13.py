# 13. Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
# preço = preço - (preço *5/100)

preço = float(input("Preço do produto:"))
desconto = preço * (5/100)
preço_final = preço - desconto
print("O preço final do seu produto é: {}".format(preço_final))
