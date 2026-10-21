#Declaração da lista
lista = [10, 20, 30]
#Acesso pelo índice(Inicia em 0)
print(lista[0])

"""
Métodos importantes em Python
"""
lista.append(40) #Adiciona um elemento ao final da lista
lista.insert(1,15) #Adiciona um elemento na posição especifica
lista.remove(20) #Remove a primeira ocorrencia de um valor
x = lista.pop() #Remove e retorna o elemento de um indice (o ultimo por padrão)
lista.count(10) #Conta quantas vezes o valor aparece na lista
lista.index(30) #Retorna o indice da primeira ocorrencia de um valor
lista.sort() #Ordena a lista no propio objeto (crescente por padrão)
lista.reverse() #Iverte a ordem dos elementos da lista
