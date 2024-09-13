class Banco:
    def __init__(self):
        self.saldo = 0
        self.extrato = []

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(f"Saque: -R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            print("Valor de saque inválido.")
            input("Presione uma tecla para continuar.")

    def exibir_extrato(self):
        print("\n--- Extrato ---")
        if not self.extrato:
            print("Nenhuma transação realizada.")
        else:
            for transacao in self.extrato:
                print(transacao)
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print("----------------\n")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: +R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")
            input("Presione uma tecla para continuar.")


    def converter_virgula(self, valor_str):
        # a se o usuário entrar com virgula o sistema converte para não da erro
        try:
            return float(valor_str.replace(',', '.'))
        except ValueError:
            print("Valor inválido.")
            return None


# Simulação das operações bancárias
banco = Banco()

while True:
    Menu="""
    1 - Depositar
    2 - Saque
    3 - Extrato
    4 - Sair
    """
    print(Menu)

    opcao = input("Qual operção deseja realizar? : ")

    if opcao == "1":
        valor_str = input("Digite o valor para depositar: R$ ")
        valor = banco.converter_virgula(valor_str)
        if valor is not None:
            banco.depositar(valor)
    elif opcao == "2":
        valor_str = input("Digite o valor para sacar: R$ ")
        valor = banco.converter_virgula(valor_str)
        if valor is not None:
            banco.sacar(valor)
    elif opcao == "3":
        banco.exibir_extrato()
        input("Presione uma tecla para continuar.")
    elif opcao == "4":
        print("Obrigado por utilizar nosso sistema bancário!")
        break
    else:
        print("Opção inválida, tente novamente.")
