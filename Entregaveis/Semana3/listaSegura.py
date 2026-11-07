# Função que adiciona um item sem alterar a lista original

def adicionar_item(lista, item):
    nova_lista = lista.copy()
    nova_lista.append(item)
    return nova_lista