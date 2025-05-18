#Gabrielly Alves Gomes - Matrícula: 20249035386
#Iago de Sousa Aragão - Matrícula: 20249014134
#Isaac Manuel Gomes Mineiro - Matrícula: 20249014170

from conta import Conta, Corrente, Poupanca

class Agencia:
    def __init__(self, numero_agencia):
        self._numero = numero_agencia
        self.lista_contas = []

    @property
    def numero(self):
        return self._numero
    
    def adicionar_conta(self, criar_conta):
        if isinstance(criar_conta, Conta):
            self.lista_contas.append(criar_conta)
        else:
            raise ValueError("Somente objetos do tipo Conta podem ser adicionados.")

    def buscar_conta(self, numero_conta):
        for conta_objeto in self.lista_contas:
            if conta_objeto.numero == numero_conta:
                return conta_objeto
        return None

    def cadastrar_conta(self, numero_nova_conta, saldo, tipo_conta="base"):
        if self.buscar_conta(numero_nova_conta):
            return None
        nova_conta = None
        if tipo_conta == "base":
            nova_conta = Conta(numero_nova_conta, saldo)
        elif tipo_conta == "corrente":
            taxa_padrao_corrente = 0.01
            nova_conta = Corrente(numero_nova_conta, saldo, taxa_padrao_corrente)
        elif tipo_conta == "poupanca":
            nova_conta = Poupanca(numero_nova_conta, saldo)
        else:
            return None
        
        if nova_conta:
            self.lista_contas.append(nova_conta)
            return nova_conta

    def relatorio(self):
        print(f"Agência: {self.numero}, Contas: {len(self.lista_contas)}, Saldo Total: R${self.saldo_total:.2f}")

    @property
    def saldo_total(self):
        return sum(conta_objeto.saldo for conta_objeto in self.lista_contas)

    def __add__(self, outra_agencia):
        if isinstance(outra_agencia, Agencia):
            total_self = sum(conta_objeto.saldo for conta_objeto in self.lista_contas)
            total_outra = sum(conta_objeto.saldo for conta_objeto in outra_agencia.lista_contas)
            return total_self + total_outra
        raise ValueError("Só é possível somar com outra agência")

    def __str__(self):
        contas_str = "\n  ".join(str(conta_objeto) for conta_objeto in self.lista_contas)
        total_saldo = sum(conta_objeto.saldo for conta_objeto in self.lista_contas)
        return f"Agência Nº {self.numero}\nContas:\n  {contas_str}\nTotal em saldo: R$ {total_saldo:.2f}"