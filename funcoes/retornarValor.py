#Devolvendo um resultado e a saída antecipada
def dobro(x):
    return x * 2
print(dobro(5)) #10

def dividir(a, b):
    if b == 0:
        return None #Saída Antecipada
    return a / b

#Retorno de vários valores
def dividir2(a, b):
    #devolve uma TUPLA
    return a //b, a % b 

q, r = dividir2(17, 5)
print(q, r) #3, 2

res = dividir2(17, 5)
print(res) #(3, 2)