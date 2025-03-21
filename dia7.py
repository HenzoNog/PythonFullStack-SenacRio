'''1'''
numero = int(input("Digite um número para a contagem REGRESSIVA"))
for i in range(numero, -1, -1):
    print(i)
'''2'''
numero = int(input("Digite um numero para ser regredido e somado no final"))
soma=0
i=1
while i <= numero:
    soma += i
    i += 1
print("Soma:", soma)

'''3'''
numero = int(input("Digite um numero para ser lido na tabuada de 1 a 10"))
for i in range(1, 11):
    resultado = numero *i
    print (f"{numero} * {i} = {resultado}")

'''4'''
numero = int(input("Digite um numero:"))
for i in range(numero, -1, -2):
    print (i)
'''5'''
numero = int(input("Digite um numero para descobrir seu fatorial:"))
fat=1
i = numero
while i <= numero:
    fat *= i
    i -= 1
print (f'O fatorial do {numero} é {fat}:')

'''6'''

numero = 0
while numero <= 10:
    numero = int(input("Digite um número maior que 10: "))
print("Número válido:", numero)

'''7'''

tamanho = int(input("Digite o tamanho do quadrado: "))
for i in range(tamanho):
    for j in range(tamanho):
        print("*", end=" ")
    print()