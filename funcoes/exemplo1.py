#Com retorno
def somar (a, b):
    return a + b #Devolve o valor

#Sem retorno
def mostrar(x):
    print(x) #Retorna None

r = somar(10,15) 
print(mostrar(7)) #imprime none
print(r) #r vale 15

#retorno antecipado
def dividir (a, b):
    if b == 0:
        return None #sai antes
    return a / b

#Devolver varios valores
def dividir2 (a, b):
    return a // b, a % b

q,r = dividir2 (7, 2) #Retorna 3 e 1
print(q, r)

#Procedimento so executa a ação
def saudar(nome):
    print(f"Olá, {nome}!") #Exibe a mensagem e não há retorno

saudar("Ana")
r = saudar("Ana")
print(r) #None