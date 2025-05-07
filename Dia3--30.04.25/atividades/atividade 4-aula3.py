import random
import string
import hashlib

class Colaborador:
    def __init__(self, nome, cpf, rg, salario):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.salario = float(salario)  # Convertendo o salário para float
        self.id_cpf = self.gerar_id_anonimo(cpf)
        self.id_rg = self.gerar_id_anonimo(rg)

    def gerar_id_anonimo(self, dado_sensivel, comprimento_id=12):
        dado_limpo = ''.join(filter(str.isalnum, dado_sensivel))
        embaralhado = ''.join(sorted(dado_limpo + str(random.randint(1000, 9999))))
        hash_obj = hashlib.sha256(embaralhado.encode())
        hash_hex = hash_obj.hexdigest()
        caracteres = string.ascii_letters + string.digits
        random.seed(hash_hex)
        return ''.join(random.choices(caracteres, k=comprimento_id))

    def __str__(self):
        return (f"👤 Nome: {self.nome}\n"
                f"🆔 ID CPF: {self.id_cpf}\n"
                f"🆔 ID RG:  {self.id_rg}\n"
                f"💰 Salário: R$ {self.salario:.2f}")

# Lista para armazenar colaboradores
colaboradores = []

def adicionar_colaborador():
    print("\n🔹 Adicionar novo colaborador")
    nome = input("Nome do colaborador: ")
    cpf = input("CPF: ")
    rg = input("RG: ")
    salario = input("Salário: ")

    colaborador = Colaborador(nome, cpf, rg, salario)
    colaboradores.append(colaborador)
    print("\n✅ Colaborador adicionado com sucesso!")
    print(colaborador)

# Loop para cadastro múltiplo
while True:
    adicionar_colaborador()
    continuar = input("\nDeseja adicionar outro colaborador? (s/n): ").strip().lower()
    if continuar != 's':
        break

# Lista final
print("\n📋 Lista de colaboradores:")
for i, c in enumerate(colaboradores, 1):
    print(f"\nColaborador {i}:")
    print(c)

# Filtro para colaboradores com salário acima de 1500
colaboradores_acima_1500 = [c for c in colaboradores if c.salario > 1500]

# Exibindo colaboradores com salário acima de 1500
print("\n💸 Colaboradores com salário acima de R$1500:")
if colaboradores_acima_1500:
    for i, c in enumerate(colaboradores_acima_1500, 1):
        print(f"\nColaborador {i}:")
        print(c)
else:
    print("Nenhum colaborador com salário acima de R$1500.")
