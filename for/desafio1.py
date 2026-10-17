"""
Crie um programa que leia 10 numeros e conte quantos sao positivos usando For
"""
positivos = 0
quantidade = int(input("Digite a quantidade de numeros que quer verificar: "))
for i in range(quantidade):
    num = int(input(f"Digite o {i+1}º numero que deseja verificar: "))
    if num > 0:
        positivos += 1
print(f"A quantidade de positivos é {positivos}")