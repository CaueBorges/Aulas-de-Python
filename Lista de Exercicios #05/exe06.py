#Escreva um programa que receba o preço de dois produtos. Calcule um desconto de 8% no
#primeiro produto, 11% no segundo e apresente o valor final a ser pago.

preço = float(input('Qual é o preço do primeiro produto? R$'))
preço2 = float(input('Qual é o preço do segundo produto? R$'))
novo = preço - (preço * 8 / 100)
novo2 = preço2 - (preço2 * 11 / 100)
print('O preço do primeiro produto com desconto é: ', novo)
print('O preço do segundo produto com desconto é: ', novo2)