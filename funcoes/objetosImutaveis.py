#int, float, str e tupla são imutáveis
def dobrar(numero):
    numero = numero * 2 #Novo objeto
    return numero

valor = 10
print(dobrar(valor)) #20
print(valor) #10