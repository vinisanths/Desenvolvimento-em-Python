nome = "start"
#nome = str(input("Digite um nome para continuar ou 'fim' para parar: "))
contadora = 0
while nome != "fim":
    nome = input("Digite um nome para continuar ou 'fim' para parar: ")
    if nome != "fim":
        contadora += 1
print(f"A quantidade de nomes digitados foi: {contadora}")