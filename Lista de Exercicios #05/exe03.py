#Escreva um algoritmo que leia o ano de nascimento de dez pessoas e no final mostre quantas
#pessoas são maiores de idade.

atual = 2021
totmaior = 0
for pess in range(1, 11):
    nasc = int(input('Em qua ano a {} pessoa nasceu?'.format(pess)))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))