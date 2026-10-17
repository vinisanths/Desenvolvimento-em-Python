"""
Parâmetros: sep muda o separador, end muda o fim da linha
"""
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")  #Saída: Olá, [nome digitado]!
idade = input("Digite sua idade: ")
print(type(idade))  #Saída: <class 'str'>
print("a","b", "c")  #Saída: a b c
print("a","b", "c", sep="-")  #Saída: a-b-c
print("Olá", end=" ")  #Saída: Olá (sem quebra de linha)
print("Mundo!")  #Saída: Mundo! (na mesma linha que "Olá")
