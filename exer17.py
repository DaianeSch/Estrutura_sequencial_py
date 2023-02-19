#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta 
# é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de 
#folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
tam=float(input('Digite o tamanho da area em metros quadrados:'))
b = 0.0
c = 0.0
litros = tam/6.0 #a cada 3 metros 1 litro

#comprar apenas latas de 18 litros;
if litros >= 18.0:
    valor1 = 80.0/18.0 #Preco a cada 1 litro
    preco1 = round(litros*valor1,2) 
    latas1 = preco1/80.0 #qtd de latas

    if litros >= 18.0 and latas1 == round(latas1):
        c = round(latas1)
        b = latas1*80.0
        print('Qtd de latas necessárias de 18L:',c)
        print('Preco latas:',b)

    else:
        if litros >= 18.0:
            c = round(latas1+0.5) #arredonda pra cima
            print('Qtd de latas de 18L:',c)
            b = c*80.0
            print('Valor:',b)

#comprar apenas galões de 3,6 litros;
if litros < 18.0:
    valor2 = 25.0/3.6
    preco2 = round(litros*valor2,2)
    latas2 = preco2/25.0
    
    if latas2 == round(latas2):
        c=round(latas2)
        b= latas2*25.0
        print('Qtd latas de 3.6L',c)
        print('Valor total:',b)
    else:
        c = round(latas2+0.5) #arredonda pra cima
        print('Vai precisar',c,'lata de 3,6 litros')
        b = c*25.0
        print('Valor:',b)
