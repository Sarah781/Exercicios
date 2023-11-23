""" Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.

Entrada
Seis valores, negativos e/ou positivos.

Saída
Imprima uma mensagem dizendo quantos valores positivos foram lidos. """

pares = 0
for i in range(5):

    n = int(input(""))
    if n%2==0:
        pares = pares + 1
print(f"{pares} valores pares")