def calcular_tmb(sexo, peso, altura, idade):
  
    if sexo.lower() == 'mulher':
        tmb = 655.1 + (9.563 * peso) + (1.850 * altura) - (4.676 * idade)
    elif sexo.lower() == 'homem':
        tmb = 66.5 + (13.75 * peso) + (5.003 * altura) - (6.775 * idade)
    else:
        raise ValueError("Sexo inválido. Use 'homem' ou 'mulher'.")
    
    return round(tmb, 2)


def calcular_tdee(tmb, nivel_atividade):

    tdee = tmb * nivel_atividade
    return round(tdee, 2)



sexo = input("Informe o sexo (homem/mulher): ")
peso = float(input("Informe o peso (kg): "))
altura = float(input("Informe a altura (cm): "))
idade = int(input("Informe a idade (anos): "))

nivel_atividade = float(input("Informe o nível de atividade (1.2 - sedentário, 1.375 - levemente ativo, 1.55 - moderadamente ativo, 1.725 - muito ativo, 1.9 - extremamente ativo): "))


tmb = calcular_tmb(sexo, peso, altura, idade)


tdee = calcular_tdee(tmb, nivel_atividade)

print(f"O TMB (Taxa de Metabolismo Basal) é de aproximadamente {tmb} kcal/dia.")
print(f"O TDEE (Total de Calorias Diárias) é de aproximadamente {tdee} kcal/dia.")