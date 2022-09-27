#Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não 
# votar este ano (não é necessário considerar o mês em que a pessoa nasceu).

nascimento = int(input('Em que ano você nasceu? '))
ano_atual = int(input('Em que ano nós estamos? '))


if ano_atual - nascimento < 16 :
    print('Você ainda não pode votar!')

else:
    print('Você pode votar este ano!')
