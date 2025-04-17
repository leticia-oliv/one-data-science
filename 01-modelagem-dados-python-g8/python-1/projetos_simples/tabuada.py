#Escreva um programa que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. Como exemplo, para o número 2, a tabuada deve ser mostrada no seguinte formato:
# Tabuada do 2:
# 2 x 1 = 2
# 2 x 2 = 4
# [...]
# 2 x 10 = 20

# ------------------------------------------------------------------------------

numero = int(input("Digite um número inteiro de 1 a 10 para ver a tabuada: "))
if numero < 1 or numero > 10:
    print('Escolha um número inteiro de 1 a 10!')
else:
    for i in range(1,11):
        resultado = numero * i
        print(f'{numero} X {i} = {resultado}')