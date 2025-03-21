'''REVISÃO CONCEITOS DA AULA 4'''

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))


media = (n1 + n2) / 2

if media >= 7:
    print("Aprovado!")
    print("Parabéns por seu esforço e dedicação.")
else:
    print("Aluno REPROVADO.")


print(f"Sua média é: {media:.2f}")