#Copia defensiva antes de alterar
def total(carrinho):
    itens = carrinho[:]
    itens.append("brinde")
    return itens

original = ["Arroz"]
novo = total(original)
print(original)
print(novo)