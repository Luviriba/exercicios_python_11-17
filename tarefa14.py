# 14. Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
# salario + (salario*15/100)

salário = float(input("Insira o valor do seu salario:"))
aumento = salário * (15/100)
print("Você recebeu um aumento de {}".format(aumento))
salário_final = salário + aumento
print("Com isso seu salário passou a ser R$ {}".format(salário_final))