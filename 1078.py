tabuada=int(input(""))

for count in range(10): 
    print("%d x %d = %d" % (count+1, tabuada, tabuada*(count+1)) )

""" count é uma variável de iteração. No contexto do loop for, a variável count é usada para percorrer os elementos de uma sequência.
range(10) gera uma sequência de números de 0 a 9 (um total de 10 números).
O loop for então itera sobre cada número gerado por range(10), e a cada iteração, a variável count assume o valor do número atual na sequência.
%dx: Este é um marcador de posição para o primeiro valor, que será substituído pelo valor de tabuada. O "d" indica que o valor deve ser um número inteiro (d de "decimal").

%d: Este é um segundo marcador de posição, que será substituído pelo valor de count+1. Novamente, o "d" indica que o valor deve ser um número inteiro.

= %d: Este é o terceiro marcador de posição, que será substituído pelo resultado da expressão tabuada * (count + 1). O "d" aqui também indica que o valor deve ser um número inteiro.

A notação % (tabuada, count+1, tabuada*(count+1)) que segue a string de formatação especifica quais valores serão substituídos nos marcadores de posição. Cada %d na string de formatação é associado a um valor na tupla fornecida após o operador %. Os valores são substituídos na ordem em que aparecem na tupla. """