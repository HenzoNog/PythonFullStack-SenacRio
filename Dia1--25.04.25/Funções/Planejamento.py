def planejar_refeicoes(tdee, objetivo):
   
    
    refeicoes = {
        "Café da manhã": tdee * 0.25,
        "Lanche da manhã": tdee * 0.10,
        "Almoço": tdee * 0.30,
        "Lanche da tarde": tdee * 0.10,
        "Jantar": tdee * 0.20,
        "Ceia": tdee * 0.05
    }

    
    if objetivo == 'perda':
        for refeicao in refeicoes:
            refeicoes[refeicao] -= refeicoes[refeicao] * 0.1  # Reduzir 10% nas refeições
    elif objetivo == 'ganho':
        for refeicao in refeicoes:
            refeicoes[refeicao] += refeicoes[refeicao] * 0.1  # Aumentar 10% nas refeições

    
    refeicoes = {refeicao: round(caloria, 2) for refeicao, caloria in refeicoes.items()}
    
    return refeicoes

tdee = float(input("Digite seu gasto calórico diário (TDEE): "))
objetivo = input("Qual o seu objetivo? (perda, manutencao ou ganho): ").lower()

refeicoes = planejar_refeicoes(tdee, objetivo)

print("\nPlanejamento calórico por refeição:")
for refeicao, calorias in refeicoes.items():
    print(f"{refeicao}: {calorias} kcal")