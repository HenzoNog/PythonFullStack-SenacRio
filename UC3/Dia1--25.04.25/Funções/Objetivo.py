def calcular_macronutrientes(tdee, objetivo):
   
    if objetivo == 'perda':
        tdee -= tdee * 0.2  # Déficit de 20% para perda de peso
    elif objetivo == 'ganho':
        tdee += tdee * 0.1  # Superávit de 10% para ganho de massa muscular
    
    proteina = tdee * 0.25 / 4  # 1g de proteína = 4 calorias
    carboidrato = tdee * 0.50 / 4  # 1g de carboidrato = 4 calorias
    gordura = tdee * 0.25 / 9  # 1g de gordura = 9 calorias
    
    return round(proteina, 2), round(carboidrato, 2), round(gordura, 2)


tdee = float(input("Digite seu gasto calórico diário (TDEE): "))
objetivo = input("Qual o seu objetivo? (perda, manutencao ou ganho): ").lower()

proteina, carboidrato, gordura = calcular_macronutrientes(tdee, objetivo)

print(f"\nDistribuição de macronutrientes para o objetivo '{objetivo}':")
print(f"Proteína: {proteina}g")
print(f"Carboidrato: {carboidrato}g")
print(f"Gordura: {gordura}g")
