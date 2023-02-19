#Tendo como dado de entrada a altura (h) de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

h = float (input('Digte sua altura:'))
genero = (input('Digite *f* se for mulher ou *m* se for homem:'))
fem = (62.1*h)-44.7
mas = (72.7*h)-58
if genero == 'f':
    cal = fem
    print (cal)
if genero == 'm':
    cal == mas
    print (cal)
