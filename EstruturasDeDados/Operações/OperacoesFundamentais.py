"""
Filtragem
"""
#Lista original de valores
lista = [10,20,5,3,42,7]
#Filtragem com list comprehension
maiores = [x for x in lista if x > 10]
print(maiores) #[20, 42]
#Mesma filtragem com filter()
pares = list(filter(lambda x: x % 2 == 0, lista))
print(pares) #10, 20, 42

"""
Ordenação
"""
#Lista fora de ordem
lista = [10,20,5,3,42,7]
# .sort() ordena a lista
lista.sort()
print(lista)
#Ordem decrescente 
lista.sort(reverse=True)
print(lista)
#sorted() devolve uma nova lista
nova = sorted(lista)
"""
União/Interseção
"""
#Dois conjuntos de valores
a = {1,2,3}
b = {3,4,5}
#União: Tudo de A e B
print(a | b) #{1, 2, 3, 4, 5}
#Interseção: o que há nos dois
print(a & b) #{3}
#Diferença: Só o que é de A
print(a - b) #{1, 2}