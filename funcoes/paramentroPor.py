#Pasagem de Parâmetros: por Tipo
#Imutaveis: int, str, tupla
def muda(x):
    x = 10 #Só o noe local
n = 5
muda(n)
print(n) #5 -> Não mudou

#Mutaveis: Listas, Dicionarios, Set
def inclui(lst):
    lst.append(4) #Altera o objeto
v = [1,2,3,]; inclui(v) 
print(v) #[1,2,3,4]

#Passagem de Parâmetros: por atribuição
#O parametro é so um novo nome
def renomeia(lista):
    lista = [9, 9] #Novo objeto
    lista.append(1) #Só o local

v = [1, 2]
renomeia(v)
print(v) #[1, 2]