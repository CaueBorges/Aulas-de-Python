#Escreva um algoritmo que receba 10 valores digitados pelo usuário e no final exiba o maior
#número.

cont = 1
maior = 0

while cont <= 10:
    num = int(input("Digite um numeros:"))
    cont += 1
    if num> maior:
        maior= num
print("O maior numero é: ", maior)