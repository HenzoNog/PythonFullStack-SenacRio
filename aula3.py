nome = 'João'
idade = 25 
print (nome , idade)

a = 10 
b = 5
print ('Soma:' , a + b)
print ('Subtração' , a - b)
print ('Multiplicação', a * b)
print ('Divisão' , a / b)

primeiro_nome = 'Maria'
sobrenome = 'Silva'
nome_completo = primeiro_nome + " " + sobrenome
print (nome_completo)

x = 15
y = 20
print ('x é maior que y?' , x > y)
print ('x é igual a y?', x == y) 

tem_carteira = True
idade = 18
tem_carro = False
pode_dirigir = idade >= 18 and tem_carteira
print('Pode dirigir?', pode_dirigir)
print('Pode dirigir e tem carro?' , pode_dirigir and tem_carro)

frase = 'Python é divertido'
print (frase.upper())
nova_frase = frase.replace('divertido' , 'poderoso')
print(nova_frase)

contador = 0 
contador += 5
contador -= 2
contador *=3
print ('Valor final do contador', contador)

a = 10
b = 20
c = 30 
media = (a + b + c) / 3
print('média:' , media)
print ('A media é maior que 15 e menor que 25?', 15 < media < 25)

nota = 75
if nota >= 60:
    print ('Aprovado')
elif nota >= 40:
    print ('Recuperação')
else:
    print ('Reprovado')

dia_da_semana = 3
dias = {
  1: 'Domingo',
  2: 'Segunda',
  3: 'Terça',
  4: 'Quarta',
  5: 'quinta',
  6: 'Sexta',
  7: 'Sábado'
}
print (dias.get(dia_da_semana, 'Dia inválido'))