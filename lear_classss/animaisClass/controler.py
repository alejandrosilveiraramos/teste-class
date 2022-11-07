
#EXERCICIO-05 crie um documento instanciando uma classe chamada animal, crie a função construtor, com a variável referência que acessa os atributos da classe no espaço alocado de memória.  defina os atributos diretamente na função construtor espécie,  gênero, idade, cor, crie um segundo documento main com variável animal 1, animal 2, animal 3 , insira valores diferentes para cada objeto, através de um input imprima no terminal o espaço  alocado de memória do objeto principal

class Animal:
    def __init__(self, especie, genero, idade, cor):
        self.especie = especie
        self.genero = genero
        self.idade = idade
        self.cor = cor