# Calculadora de troco
compra = float(input("Digite o valor da compra: R$ "))
pago = float(input("Digite o valor pago: R$ "))

troco = pago - compra

if troco < 0:
    print(f"Valor pago insuficiente. Faltam R$ {troco}")
else:
    print(f"Troco: R$ {troco}")