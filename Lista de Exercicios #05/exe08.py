#Escreva um algoritmo que receba um nome e três notas e atenda exiba uma mensagem
#diferente para cada um dos casos a seguir:
#A) Se a média for maior que 7, exiba a mensagem “Parabéns (nome)! Você foi aprovado”;
#B) Se a média for menor que 7 e maior que 5, exiba a mensagem “Você ficou com média
#(media) e está de recuperação;
#C) Se a média for menor que 5, exiba a mensagem “(Nome), você está reprovado”.

nome = str(input("Digite um nome:" ))
for n in range(1, 4):
    n = float(input('Digite a {} nota: '.format(n)))
    media = (n+n+n)/3
if media >= 7:
     print("Parabens {} : Voce foi aprovado ".format(nome))
elif 7 > media >= 5:
     print("Voce ficou com media {} e esta de recuperaçao ".format(media))
elif media < 5:
     print("{}, voce esta reprovado".format(nome))