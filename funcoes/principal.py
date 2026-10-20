#modulo.py -> usa calculadora
from modulo import calculadora as c
print(c.somar(2, 3)) #5
print(c.PI) #3.14159

#Importando so o que precisa
from modulo.calculadora import somar
print(somar(2, 3)) #5