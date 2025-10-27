class Registro:
    def __init__(self, agencia: str, conta: str):
        self._agencia = agencia
        self._conta = conta

    def getAgencia(self):
        return self._agencia

    def getConta(self):
        return self._conta

    def __str__(self):
        return f"Agência: {self._agencia}, Conta: {self._conta}"


class Conta:
    def __init__(self, nome: str, registro: Registro, saldo: float):
        self._nome = nome
        self._registro = registro
        self._saldo = saldo
        self._historico = []

    def getSaldo(self) -> float:
        return self._saldo

    def getNome(self) -> str:
        return self._nome

    def getRegistro(self) -> Registro:
        return self._registro

    def creditar(self, valor: float):
        if valor > 0:
            self._saldo += valor
            self._historico.append(f"Crédito de R$ {valor:.2f}")
        else:
            print("Valor inválido para crédito.")

    def debitar(self, valor: float):
        if valor <= self._saldo and valor > 0:
            self._saldo -= valor
            self._historico.append(f"Débito de R$ {valor:.2f}")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def extrato(self):
        print(f"\nExtrato de {self._nome}:")
        for transacao in self._historico:
            print(f"  - {transacao}")
        print(f"Saldo atual: R$ {self._saldo:.2f}\n")

    def __str__(self):
        return f"{self._nome} ({self._registro}) | Saldo: R$ {self._saldo:.2f}"


class Digital(Conta):
    def __init__(self, nome: str, registro: Registro, saldo: float):
        super().__init__(nome, registro, saldo)


class Corrente(Conta):
    def __init__(self, nome: str, registro: Registro, saldo: float, limite: float, taxa_manutencao: float):
        super().__init__(nome, registro, saldo)
        self._limite = limite
        self._taxa_manutencao = taxa_manutencao

    def limiteDisponivel(self) -> float:
        return self._limite + self._saldo

    def cobrarTaxa(self):
        self._saldo -= self._taxa_manutencao
        self._historico.append(f"Cobrança de taxa de manutenção: R$ {self._taxa_manutencao:.2f}")

    def __str__(self):
        return f"{self._nome} (Corrente) | {self._registro} | Saldo: R$ {self._saldo:.2f} | Limite: R$ {self._limite:.2f}"


class Poupanca(Conta):
    def __init__(self, nome: str, registro: Registro, saldo: float, taxa_rendimento: float):
        super().__init__(nome, registro, saldo)
        self._taxa_rendimento = taxa_rendimento

    def calcularRendimento(self) -> float:
        return self._saldo * self._taxa_rendimento

    def aplicarRendimento(self):
        rendimento = self.calcularRendimento()
        self._saldo += rendimento
        self._historico.append(f"Rendimento aplicado: R$ {rendimento:.2f}")

    def __str__(self):
        return f"{self._nome} (Poupança) | {self._registro} | Saldo: R$ {self._saldo:.2f}"


class Banco:
    def __init__(self, contas: list = None):
        self._contas = contas if contas else []

    def cadastrar(self, conta: Conta):
        self._contas.append(conta)
        print(f"Conta cadastrada: {conta.getNome()}")

    def procurarConta(self, registro: Registro):
        for conta in self._contas:
            if (conta.getRegistro().getAgencia() == registro.getAgencia() and
                conta.getRegistro().getConta() == registro.getConta()):
                return conta
        return None

    def procurarPorNome(self, nome: str):
        return [c for c in self._contas if nome.lower() in c.getNome().lower()]

    def transferir(self, origem: Conta, destino: Conta, valor: float):
        if valor <= 0:
            print("Valor inválido para transferência.")
            return
        if origem.getSaldo() < valor:
            print("Saldo insuficiente para transferência.")
            return
        origem.debitar(valor)
        destino.creditar(valor)
        print(f"Transferência de R$ {valor:.2f} realizada de {origem.getNome()} para {destino.getNome()}.")

    def aplicarRendimentos(self):
        for conta in self._contas:
            if isinstance(conta, Poupanca):
                conta.aplicarRendimento()
                print(f"Rendimento aplicado para {conta.getNome()}.")

    def cobrarTaxas(self):
        for conta in self._contas:
            if isinstance(conta, Corrente):
                conta.cobrarTaxa()
                print(f"Taxa cobrada de {conta.getNome()}.")

    def listarContas(self):
        for conta in self._contas:
            print(conta)
