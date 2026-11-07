# Script principal que importa e usa os módulos

import calculadora
import utilidades
from listaSegura import adicionar_item


print("Soma:", calculadora.somar(10, 5))
print("Subtração:", calculadora.subtrair(10, 5))
print("Multiplicação:", calculadora.multiplicar(10, 5))
print("Divisão:", calculadora.dividir(10, 2))
print("Divisão por zero:", calculadora.dividir(10, 0))


print("Temperatura em Fahrenheit:", utilidades.converter_temperatura(25))
print("Senha válida:", utilidades.validar_senha("abc12345"))
print("Total da compra:", utilidades.calcular_total(10, 20, 30))
utilidades.ficha_aluno(nome="Maria", idade=20, curso="Python")

#Lista segura
numeros = [1, 2, 3]
nova_lista = adicionar_item(numeros, 4)

print("Lista original:", numeros)
print("Nova lista:", nova_lista)