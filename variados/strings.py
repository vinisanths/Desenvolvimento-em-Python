#Concatenação
nome = "João"
sauda = "Olá, " + nome + "!"  #Concatenação com +
print(sauda)  #Saída: Olá, João!
#F-strings
idade = 25
nome2 = "Carlos"
print(f"Meu nome é {nome2} e eu tenho {idade} anos.")  #Saída: Meu nome é Carlos e eu tenho 25 anos.
#Formatação com format()
preco = 19.999
print(f"O preço do produto é R$ {preco:.2f}")  #Saída: O preço do produto é R$ 20.00
pct = 0.1234
print(f"A porcentagem é {pct:.2%}")  #Saída: A porcentagem é 12.34%
#Imutabilidade e Métodos de String
p = "Python" 
print(p)
#p[0] = "J" #Isso vai gerar um erro, pois strings são imutáveis
nova = "J" + p[1:]  #Cria uma nova string com a primeira letra alterada
print(nova)  #Saída: Jython
#Métodos
p = " Python "
print(p.upper())  #Saída: PYTHON
print(p.lower())  #Saída: python
print(p.capitalize())  #Saída: Python
print(p.replace("thon", "py"))  #Saída: Pypy
print(p.split("y"))  #Saída: ['P', 'thon']
print(p.find("t"))  #Saída: 2
print(p.strip())  #Saída: Python
p.find("z")  #Saída: -1 (não encontrado)
p.count("o")  #Saída: 1 (quantas vezes o caractere aparece na string)


