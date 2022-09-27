#6. Seja criativo ao desenvolver este programa.

# Lista de Convidados

convidados = ["Nathi", "Leo", "Felipe", "Mari", "João"]


# Convite

for nome in convidados:
    mensagem = f"Bora lanchar, {nome}?"
    print(mensagem)
    
# Quem não poderá ir

    print("João: Infelizmente não posso ir!")
    print("Nathi: Infelizmente não posso ir!")
    
# Modifique sua lista, substitua os desistentes por novos convidados.

    convidados[0] = "Rayssa"
    convidados[5] = "Jayane"
    
    
# Convite

for nome in convidados:
    mensagem = f"Bora lanchar, {nome.upper()}?"
    print(mensagem)
    
    
