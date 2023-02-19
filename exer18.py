#Faça um programa que peça o tamanho de um arquivo para download (em MB)
# e a velocidade de um link de Internet (em Mbps), calcule e informe o 
#tempo aproximado de download do arquivo usando este link (em minutos).

tamb = float(input('Informe o tamanho do arquivo em MB:'))
link = float(input('Informe vel da internet em Mbps:'))

cal= tamb/(link/8.0)
print(cal,'segundos')

