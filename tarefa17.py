# 17. Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

aluno1 = str(input("Primeiro aluno: "))
aluno2 = str(input("Segundo aluno: "))
aluno3 = str(input("Terceiro aluno: "))
aluno4 = str(input("Quarto aluno: "))

sorteado = random.randrange(0,4)
if sorteado == 0:
    print(aluno1)
elif sorteado == 1:
    print(aluno2)
elif sorteado == 2:
    print(aluno3)
else:
    print(aluno4)