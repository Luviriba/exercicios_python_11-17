# 15. Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
# farenheit é ((9*celsius)/5)+32
# Kelvin é (°C + 273,15 )= K
celsius =  float(input("temperatura: "))
farenheit = ((celsius * 9)/5)+32
kelvin = (celsius + 273.15)
print("{} graus Celsius e igual a {} farenheit".format(celsius, farenheit))
print("{} graus Celsius e igual a {} kelvin".format(celsius, kelvin))
