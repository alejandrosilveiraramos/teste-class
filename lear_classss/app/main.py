#_   EXERCICIO-01 crie um documento instanciando uma classe chamada conta, crie a função construtor, com a variável referência que acessa os atributos da classe no espaço alocado de memória, acessando diretamente o objeto de conta insira dados internos na função através da variável referência padrão, e insira atributos recebendo valores internos número, titular, saldo, limite.

class Conta:
    def __init__(self, numberPerson, titular, balance, limit):
        self.numberPerson = numberPerson
        self.titular = titular
        self.balance = balance
        self.limit = limit

