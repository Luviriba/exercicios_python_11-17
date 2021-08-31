# 12. Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input("largura da parede: "))
altura = float(input("altura da parede: "))
area_da_parede = largura * altura
litros_tinta = area_da_parede / 2
print("Você precisara de {} litros de tinta para pintar uma parede de {} m².".format(litros_tinta, area_da_parede))
