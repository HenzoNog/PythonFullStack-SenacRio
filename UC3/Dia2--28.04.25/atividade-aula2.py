class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.concluida = False

    def __str__(self):
        status = "✓" if self.concluida else " "
        return f"[{status}] {self.descricao}"

class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, descricao):
        tarefa = Tarefa(descricao)
        self.tarefas.append(tarefa)
        print("Tarefa adicionada!")

    def listar_tarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\nLista de Tarefas:")
            for i, tarefa in enumerate(self.tarefas, 1):
                print(f"{i}. {tarefa}")

    def marcar_concluida(self, numero_tarefa):
        if 0 <= numero_tarefa < len(self.tarefas):
            self.tarefas[numero_tarefa].concluida = True
            print("Tarefa marcada como concluída!")
        else:
            print("Número inválido.")

    def remover_tarefa(self, numero_tarefa):
        if 0 <= numero_tarefa < len(self.tarefas):
            removida = self.tarefas.pop(numero_tarefa)
            print(f"Tarefa '{removida.descricao}' removida.")
        else:
            print("Número inválido.")

def menu():
    gerenciador = GerenciadorTarefas()
    
    while True:
        print("\nGerenciador de Tarefas")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar como concluída")
        print("4. Remover tarefa")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            descricao = input("Digite a nova tarefa: ")
            gerenciador.adicionar_tarefa(descricao)
        
        elif opcao == '2':
            gerenciador.listar_tarefas()
        
        elif opcao == '3':
            if not gerenciador.tarefas:
                print("Nenhuma tarefa para marcar.")
            else:
                try:
                    num = int(input("Número da tarefa concluída: ")) - 1
                    gerenciador.marcar_concluida(num)
                except ValueError:
                    print("Digite um número válido.")
        
        elif opcao == '4':
            if not gerenciador.tarefas:
                print("Nenhuma tarefa para remover.")
            else:
                try:
                    num = int(input("Número da tarefa a remover: ")) - 1
                    gerenciador.remover_tarefa(num)
                except ValueError:
                    print("Digite um número válido.")
        
        elif opcao == '5':
            print("Saindo do gerenciador...")
            break
        
        else:
            print("Opção inválida!")

menu()
