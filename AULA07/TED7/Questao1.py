#As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. 
# Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

print('Maçã por R$1,30 a unidade! Comprando a partir de uma dúzia, você leva por apenas R$1 cada.')

maçãs = int(input('Quantas maçãs você quer levar? '))

preco_real = 1.30
preco_promocional = 1.00

valor1 = preco_real * maçãs
valor2 = preco_promocional * maçãs 

if maçãs < 12 :
    print(f'Sua compra ficou no valor de: {valor1} ')

else:
    print(f'Sua compra ficou no valor de: {valor2}')    
