# 11. Faça um programa que insira um valor em reais, e faça ele converter o valor para dólar, mostrando quantos
# dólares podem ser comprados com aquela quantia. (Valor para ser usado do dólar no exercício: 5.30)

real = float(input("valor"))
dolar = 5.30
conver = (real / dolar)
euro = 6.33
conver1 = (real / euro)
print("Você pode comprar {} Dolares com {} Reais".format(conver, real))
print("você também pode comprar {} Euros com {} Reais".format(conver1, real))
