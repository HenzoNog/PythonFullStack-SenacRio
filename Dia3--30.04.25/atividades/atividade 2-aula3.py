def contar_por_categoria(lista_produtos):
    contagem = {}
    for produto in lista_produtos:
        categoria = produto["categoria"]
        if categoria in contagem:
            contagem[categoria] += 1
        else:
            contagem[categoria] = 1
    return contagem

# Lista de produtos com categorias
produtos = [
    {"nome": "Notebook", "preco": 3500, "categoria": "Eletrônicos"},
    {"nome": "Mouse", "preco": 150, "categoria": "Acessórios"},
    {"nome": "Teclado", "preco": 200, "categoria": "Acessórios"},
    {"nome": "Monitor", "preco": 1200, "categoria": "Eletrônicos"},
    {"nome": "Cabo HDMI", "preco": 50, "categoria": "Acessórios"},
    {"nome": "Impressora", "preco": 900, "categoria": "Periféricos"},
]

# Contagem por categoria
contagem = contar_por_categoria(produtos)

print(contagem)