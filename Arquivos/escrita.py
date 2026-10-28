#write -> Escreve uma string
with open("saida.txt", "w", encoding="utf-8") as f:
    f.write("Primeira linha\n")
    f.write("Segunda linha\n")

#Append (adiciona ao final)
with open("saida.txt", "w", encoding="utf-8") as f:
    f.write("Terceira linha\n")

#writelines(lista) -> Escreve uma lista de strings
linhas = ["Linha A\n", "Linha B\n", "Linha C\n"]
with open("saida.txt", "w", encoding="utf-8") as f:
    f.writelines(linhas)

#Append (adiciona ao final)
with open("saida.txt", "a", encoding="utf-8") as f:
    f.write("Terceira linha\n")