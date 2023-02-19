#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% 
# para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.
hora = float(input('Valor da hora trabalhada:'))
trab = float(input('Numero de horas trabalhadas:'))
salario = (hora*trab)
print ('Salario bruto é igual a:R$',salario)
#INSS
print ('Descontos')
inss = round(salario*0.08,2)
print ('INSS (8%):R$',inss)
#IR
ir = salario * 0.11
print('IR(11%):R$',ir)
#sindicato
sin = salario * 0.05
print ('Sindicato (5%):R$',sin)
#salario liquido
desc = inss+ir+sin
liq = salario-desc
print ('Salario liquido:R$',liq)



