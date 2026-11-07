#Estruturas de Dados

produtos = []

quantidade = int(input("Quantos produtos deseja cadastrar? "))

for i in range(quantidade):
    print("\nProduto", i + 1)
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: R$ "))
    categoria = input("Categoria do produto: ")

    produto = [nome, preco, categoria]
    produtos.append(produto)

valor = float(input("\nDigite o valor para filtrar os produtos: R$ "))

print("\nProdutos acima do valor informado:")
for produto in produtos:
    if produto[1] > valor:
        print(f"Nome: {produto[0]} | Preço: R$ {produto[1]:.2f} | Categoria: {produto[2]}")

print("\nProdutos abaixo do valor informado:")
for produto in produtos:
    if produto[1] < valor:
        print(f"Nome: {produto[0]} | Preço: R$ {produto[1]:.2f} | Categoria: {produto[2]}")


produtos_crescente = sorted(produtos, key=lambda produto: produto[1])
produtos_decrescente = sorted(produtos, key=lambda produto: produto[1], reverse=True)

print("\nProdutos em ordem crescente de preço:")
for produto in produtos_crescente:
    print(f"{produto[0]} - R$ {produto[1]:.2f}")

print("\nProdutos em ordem decrescente de preço:")
for produto in produtos_decrescente:
    print(f"{produto[0]} - R$ {produto[1]:.2f}")

# Conjuntos
categorias = set()

for produto in produtos:
    categorias.add(produto[2])

print("\nCategorias únicas:")
for categoria in categorias:
    print(categoria)

# Tupla 
precos = []

for produto in produtos:
    precos.append(produto[1])

estatisticas = (min(precos), max(precos), sum(precos) / len(precos))

# Relatório final
print("\n===== RELATÓRIO FINAL =====")

for produto in produtos:
    print(f"Produto: {produto[0]}")
    print(f"Preço: R$ {produto[1]:.2f}")
    print(f"Categoria: {produto[2]}")
    print("--------------------------")

print(f"Menor preço: R$ {estatisticas[0]:.2f}")
print(f"Maior preço: R$ {estatisticas[1]:.2f}")
print(f"Média dos preços: R$ {estatisticas[2]:.2f}")
print(f"Total de produtos cadastrados: {len(produtos)}")
print(f"Total de categorias únicas: {len(categorias)}")