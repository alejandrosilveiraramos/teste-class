#EXERCICIO-02 crie um documento instanciando uma classe chamada conta, crie a função construtor, com a variável referência que acessa os atributos da classe no espaço alocado de memória,  defina os atributos diretamente na função construtor número, titular, saldo, limite, crie um segundo documento main com variável conta 1, conta 2, conta 3 , insira valores diferentes para cada objeto, imprima no terminal o espaço  alocado de memória do objeto principal , e de cada variável de referência para o objeto!



class Conta:
    def __init__(self, numberPerson, titular, balance, limit):
        self.numberPerson = numberPerson
        self.titular = titular
        self.balance = balance
        self.limit = limit



conta = Conta('333123', 'Alberto', 1500, 5000)
conta2 = Conta('666123', 'Flavio', 2500, 30000)
conta3 = Conta('444123', 'Bruna', 3000, 35000)

print(conta.titular)
print(conta2.titular)
print(conta3.titular)
