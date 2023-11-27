#Dividindo x por y
#Escreva um algoritmo que leia 2 números e imprima o resultado da divisão do primeiro pelo segundo. Caso não for possível mostre a mensagem “divisao impossivel” para os valores em questão.

#Entrada
#A entrada contém um número inteiro N. Este N será a quantidade de pares de valores inteiros (X e Y) que serão lidos em seguida.

#Saída
#Para cada caso mostre o resultado da divisão com um dígito após o ponto decimal, ou “divisao impossivel” caso não seja possível efetuar o cálculo

x, y = map(int, input().split()) #A função map(int, ...) é usada para converter cada string na lista para um inteiro. Finalmente, os valores convertidos são atribuídos às variáveis x e y. A função split() é então usada para dividir a entrada em uma lista de strings com base nos espaços.
if y == 0:
    print('divisao impossivel')
else:
    resultado = x / y
    print(f"{resultado:.1f}") #:.1f é usado para imprimir um número flutuante com 1 casa decimal.