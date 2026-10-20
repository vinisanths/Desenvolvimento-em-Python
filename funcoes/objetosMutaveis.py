#lista, Dicionario e Set(conjuntos): mutaveis
def add(lista, item):
    lista.append(item) #Altera objeto

compras = ["arroz"]
add(compras, "Feijao")
print(compras)

#Copia defensiva: Protege o original
add(compras[:], "Café")
print(compras)

#Evitando bugs com mutáveis
def add(item, lista=[]):
    lista.append(item)
    return lista

print(add("a"))
print(add("b"))
