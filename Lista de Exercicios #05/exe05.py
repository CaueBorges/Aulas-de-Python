#Escreva um algoritmo para calcular o fatorial de um número. Se o usuário digitou, por exemplo,
#o valor 5, o resultado a ser exibido pelo algoritmo é: 5! é igual a 120

n = int(input("Digite um numero para calcular seu fatorial: "))
c = n
f = 1
while c > 0:
    f *= c
    c -= 1
print('O farorial é: {} '.format(f))