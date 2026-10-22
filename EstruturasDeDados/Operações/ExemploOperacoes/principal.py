from adicionar import adicionar
from remover import remover
from atualizar import atualizar
from iterar import iterar
from pertencimento import existe

estoque = ["Mouse", "Mose", "Hd"]
adicionar(estoque, "Teclado")
atualizar(estoque, "Mose", "Mouse2")
remover(estoque, "Hd")
if existe(estoque, "Teclado"):
    iterar(estoque) #Relátorio Final