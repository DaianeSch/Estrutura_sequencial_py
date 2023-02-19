#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

num1 = int(input('Digite primeiro numero inteiro:'))
num2= int(input('Digite segundo numero inteiro:'))
numr = int (input('Digite um numero inteiro:'))

##o produto do dobro do primeiro com metade do segundo .
prod = ((num1**2)*(num2/2))
print('O produto do dobro do primeiro com metade do segundo:',prod)

#a soma do triplo do primeiro com o terceiro.
trip = ((num1*3)+numr)
print('A soma do triplo do primeiro com o terceiro:',trip)

#o terceiro elevado ao cubo.
terc = (numr**3)
print('o terceiro elevado ao cubo:',terc)



