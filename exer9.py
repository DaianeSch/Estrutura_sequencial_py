#Faça um Programa que peça a temperatura em graus Fahrenheit, 
#transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).
f = float (input('Temperatura em F°:'))
c = round(5.0*((f-32.0)/9.0),2)
print (c,'C°')

