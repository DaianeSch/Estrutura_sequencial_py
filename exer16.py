#Faça um programa para uma loja de tintas. O programa deverá pedir 
# o tamanho em metros quadrados da área a ser pintada. Considere que a 
# cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a 
# tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe 
# ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
tam=float(input('Digite o tamanho da area em metros quadrados:'))
b = 0.0
c = 0.0
litros = tam/3 #a cada 3 metros 1 litro
valorl = 80.0/18 #Preco a cada 1 litro
preco = round(litros*valorl,2) 
latas = preco/80 #qtd de latas

if litros <= 18.0: 
    print('Latas:1')
    print('Valor: R$ 80.0')

if litros > 18.0 and latas == round(latas):
    c = round(latas)
    b = latas*80.0
    print('Qtd de latas necessárias:',c)
    print('Preco latas:',b)

else:
    if litros > 18.0:
        c = round(latas+0.5) #arredonda pra cima
        print('Qtd de latas:',c)
        b = c*80.0
        print('Valor:',b)

