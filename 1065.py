#Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

#Entrada
#O arquivo de entrada contém 5 valores inteiros quaisquer.

#Saída
#Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.

#7 -5  6 -4 12

""" n1=int(input(""))
n2=int(input(""))
n3=int(input(""))
n4=int(input(""))
n5=int(input(""))

if n1%2==0:
    pares = 1
else:
    pares = 0
    
if n2%2==0:
    pares = pares + 1

if n3%2==0:
    pares = pares + 1

if n4%2==0:
    pares = pares + 1

if n5%2==0:
    pares = pares + 1


print(f"{pares} valores pares") """

pares = 0
for i in range(5):

    n = int(input(""))
    if n%2==0:
        pares = pares + 1
    else:
        pares = pares + 0
print(f"{pares} valores pares")


