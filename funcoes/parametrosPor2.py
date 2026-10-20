#Posicionais e Obrigatorios
"""
A ordem dos argumentos define o valor de cada paramentro
"""
def saudar(nome, sobrenome):
    return nome + " " + sobrenome

print(saudar("Ana", "Lu"))

print(saudar("Lu", "Ana"))

#Parametros nomeados
"""
Com o nome do parametro, a ordem nao importa
"""
def saudar2(nome, sobrenome):
    return nome + " " + sobrenome

print(saudar2(sobrenome="Lu", nome="Ana"))

#Parametros com valor padrão
"""
Sem o argumento, o python usa o valor definido
"""
def criar(nome, ativo=True):
    if ativo:
        s = "Disponível"
    else:
        s = "Esgotado"
    return nome + " - " + s

print(criar("Caneta"))
print(criar("Caneta", False))

#Parametros dinamicos: *Args
"""
Quando você não sabe quantos argumentos virão
"""
def somar(*numeros):
    #Numeros chega como uma TUPLA
    return sum(numeros)

print(somar(1,2,3,4)) #10
print(somar(0)) #0

valores = [1,2,3]
print(somar(*valores)) #6

#Parametros dinamicos: **Kwargs
"""
Argumentos nomeados variaveis chegam como um dicionario
"""
def perfil(**dados):
    #Dados chegam como um DICIONARIO
    for chave, valor in dados.items():
        print(chave, ":", valor)

perfil(nome="Ana", idade=25)

#Combinando *Args e *Kwargs
"""
A ordem correta dos parametros na assinatura da função
"""
def rel(titulo, *itens, fmt="txt", **extras):
    print(titulo, fmt)
    print(itens) #Tupla
    print(extras) #Dicionario

rel("Vendas", "Jan", "Fev", fmt="pdf", autor="Ana")