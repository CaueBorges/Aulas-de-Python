#Escreva um algoritmo que receba dois números e exiba para o usuário todos os valores
#intermediários a eles, veja exemplo:
#Primeiro número: 5
#Segundo número: 15
#Resultado: 6 7 8 9 10 11 12 13 14

n = int(input("Digite um numero: "))
n1 = int(input("Digite outro numero: "))
for cont in range(n, n1):
    print(cont)