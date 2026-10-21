#Declaração da Tupla (Parenteses)
ponto = (10, 20, 30)
#Acesso pelo indice (inicia em 0)
print(ponto[0]) #imprime 10
#Imprime a tupla toda
print(ponto)
#Percorrendo a Tupla 
for x in ponto:
    print(x)
"""
Métodos Importantes em python
"""
ponto.count(10) #Conta quantas vezes um valor aparece na tupla
ponto.index(20) #Retorna o indice da primeira ocorrencia do valor
len(ponto) #Retorna a quantidade de elementos da tupla
max(ponto) #Retorna o  maior valor da Tupla
min(ponto) #Retorna o  menor valor da Tupla
sum(ponto) #Soma todos os valores numericos da tupla
sorted(ponto) #Retorna uma lista com os elemntos ordenados
tuple([1,2,3]) #Converte uma lista(ou outro iteravel) em uma tupla 