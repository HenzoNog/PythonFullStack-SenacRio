def filtrar_produtos_caros(lista_produtos, preco_minimo=1000):
    return [produto for produto in lista_produtos if produto["preco"] > preco_minimo]

produtos = [
    {"nome": "Notebook", "preco": 3500},
    {"nome": "Mouse", "preco": 150},
    {"nome": "Teclado", "preco": 200},
    {"nome": "Monitor", "preco": 1200},
    {"nome": "Cabo HDMI", "preco": 50}
]

produtos_filtrados = filtrar_produtos_caros(produtos)

print(produtos_filtrados)