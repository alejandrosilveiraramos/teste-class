#EXERCICIO-03 crie um documento instanciando uma classe chamada pessoa, crie a função construtor, com a variável referência que acessa os atributos da classe no espaço alocado de memória.  defina os atributos diretamente na função construtor nome, SobreNome, idade, cpf, crie um segundo documento main com variável pessoa 1, pessoa 2, pessoa 3 , insira valores diferentes para cada objeto, imprima no terminal o espaço  alocado de memória do objeto principal , do objeto principal  e de cada variável de referência para o objeto!



class Person:
    def __init__(self, nome, sobreNome, idade, cpf):
        self.nome = nome
        self.sobreNome = sobreNome
        self.idade = idade
        self.cpf = cpf



pessoa = Person('alejandro', 'Alberto', 15, '35289526447')
pessoa2 = Person('Flavio', 'Ausgusto', 25, '80833965913')
pessoa3 = Person('Bruna', 'Davila', 35, '23515338608')

print(pessoa.cpf)
print(pessoa2.cpf)
print(pessoa3.cpf)
