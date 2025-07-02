class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None

class ListaEspera:
    def __init__(self):
        self.head = None
        self.contador_verde = 1
        self.contador_amarelo = 201

    def inserirSemPrioridade(self, nodo):
        if self.head is None:
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = nodo

    def inserirComPrioridade(self, nodo):
        if self.head is None or self.head.cor == "V":
            nodo.proximo = self.head
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo and atual.proximo.cor == "A":
                atual = atual.proximo
            nodo.proximo = atual.proximo
            atual.proximo = nodo

    def inserir(self):
        cor = input("Digite a cor do cartão (A para amarelo, V para verde): ").upper()
        if cor == "V":
            numero = self.contador_verde
            self.contador_verde += 1
        elif cor == "A":
            numero = self.contador_amarelo
            self.contador_amarelo += 1
        else:
            print("Cor inválida.")
            return

        novo_nodo = Nodo(numero, cor)
        if self.head is None:
            self.head = novo_nodo
        elif cor == "V":
            self.inserirSemPrioridade(novo_nodo)
        elif cor == "A":
            self.inserirComPrioridade(novo_nodo)

    def imprimirListaEspera(self):
        atual = self.head
        print("Fila de Espera:")
        while atual:
            print(f"Cartão {atual.cor}-{atual.numero}")
            atual = atual.proximo

    def atenderPaciente(self):
        if self.head is None:
            print("Nenhum paciente na fila.")
            return
        paciente = self.head
        self.head = self.head.proximo
        print(f"Chamando paciente do cartão {paciente.cor}-{paciente.numero} para atendimento.")

def menu():
    lista = ListaEspera()
    while True:
        print("\n1 – Adicionar paciente à fila")
        print("2 – Mostrar pacientes na fila")
        print("3 – Chamar paciente")
        print("4 – Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            lista.inserir()
        elif opcao == "2":
            lista.imprimirListaEspera()
        elif opcao == "3":
            lista.atenderPaciente()
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")


menu()
