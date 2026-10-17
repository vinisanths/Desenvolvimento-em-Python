nota = float(input("Digite uma nota entre 0 e 10: "))
while nota < 0.0 or nota > 10.0:
    print(f"Erro! Nota inválida.")
    nota = float(input("Digite a novamente uma nota válida: "))

print(f"Nota gravada com sucesso: {nota}")
             