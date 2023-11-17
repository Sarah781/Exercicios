""" Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha, inclusive o X ser for o caso.

Entrada
A entrada será um valor inteiro positivo.

Saída
A saída será uma sequência de seis números ímpares. """

x = int(input())
for i in range(6):
    if x % 2 == 0:
        x += 1
        print(x)
    else:
        print(x)
    x += 2