
#EXERCICIO-05 crie um documento instanciando uma classe chamada animal, crie a função construtor, com a variável referência que acessa os atributos da classe no espaço alocado de memória.  defina os atributos diretamente na função construtor espécie,  gênero, idade, cor, crie um segundo documento main com variável animal 1, animal 2, animal 3 , insira valores diferentes para cada objeto, através de um input imprima no terminal o espaço  alocado de memória do objeto principal

class Carro:
    def __init__(self, marca, modelo, valor):
        self.marca = marca
        self.modelo = modelo
        self.valor = valor 