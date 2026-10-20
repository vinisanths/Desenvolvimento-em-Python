#Forçando parametros só posicionais ou só nomeados
def conf(ip, /, porta, *, modo= True):
    print(ip, porta, modo)

conf("10.0.0.1", 8080, modo=False) #OK

# conf("10.0.0.1", ) -> Erro
# conf("10.0.0.1", 80, True) -> Erro

#Desempacotamento com * e ** na hora da chamada
def media(a,b,c):
    return (a + b + c) / 3

notas = [8, 6, 10]
print(media(*notas)) #8

dados = {"a": 8,
         "b": 6,
         "c": 10}

print(media(**dados)) #8