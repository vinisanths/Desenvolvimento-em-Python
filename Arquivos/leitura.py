#Sintaxe básica
#arquivo = open("nome.txt", "modo", encoding="utf-8")

#Exemplo abrindo para leitura
# with print(conteudo) open("dados.txt", "r", encoding="utf-8") as f:
#     conteudo = f.read()

#read() -> lê todo o conteudo como uma string
with open("dados.txt", "r", encoding="utf-8") as f:
    print(f.read())
print("\n")

#readline() -> lê uma linha por vez
with open("dados.txt", "r", encoding="utf-8") as f:
    print(f.readline()) #Lê a 1º linha
    print(f.readline()) #Lê a 2º linha 
print("\n")

#readlinhas() -> Retorna uma lista com todas as linhas
with open("dados.txt", "r", encoding="utf-8") as f:
    linhas = f.readlines()
    print(linhas) #['linha1\n', 'linhas2\n'...]
print("\n")

#Iteração direta mais eficiente
with open("dados.txt", "r", encoding="utf-8") as f:
    for linha in f:
        print(linha.strip())

