#Classificador de Cliente
idade = int(input("Digite a idade: "))
renda = float(input("Digite a renda: R$ "))

if idade < 18:
    print("Categoria: Bronze")
elif renda < 2000:
    print("Categoria: Prata")
elif renda < 5000:
    print("Categoria: Ouro")
else:
    print("Categoria: Diamante")