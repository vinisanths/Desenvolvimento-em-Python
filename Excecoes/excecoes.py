try:
    #Código que pode falhar
    numero = int(input("Digite um numero: "))
    resultado = 10 / numero
except ValueError:
    print("Valor inválido!")
except ZeroDivisionError:
    print("Não pode dividir por zero!")
else:
    print("Resultado: ", resultado)
finally:
    print("Fim da execução")