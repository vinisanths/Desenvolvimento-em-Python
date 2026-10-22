#Declaração do conjunto {Chaves}
frutas = {"Maca", "Uva", "Maca", "Tomate"}
legumes = {"Abobora", "Cenoura", "Beterraba", "Tomate"}
#Duplicatas são eliminadas
print(frutas) #Maca, Uva
#Teste de pertinecia(Acesso)
print("Uva" in frutas) #True
for f in frutas:
    print(f)

"""
Métodos Importantes
"""
print(frutas.add("Pera")) #Adiciona um elemento ao conjunto
print(frutas.remove("Uva")) #Remove o elemento; Erro se ele não existir
print(frutas.discard("Uva")) #Remove o elemento sem gerar erro
print(frutas.union(legumes)) #Une dois conjuntos (Todos os itens)
print(frutas.intersection(legumes)) #Retorna os itens comuns aos dois conjuntos
print(frutas.difference(legumes)) #Retorna os itens que estão só em frutas
print(len(frutas)) #Retorna a quantidade de itens unicos