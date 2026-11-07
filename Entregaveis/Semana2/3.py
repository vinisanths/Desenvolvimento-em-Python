# Análise de Números
soma = 0
maior = 0
menor = 0

for i in range(5):
    numero = float(input("Digite um número: "))
    soma = soma + numero

    if i == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

media = soma / 5

print("Soma:", soma)
print("Média:", media)
print("Maior:", maior)
print("Menor:", menor)