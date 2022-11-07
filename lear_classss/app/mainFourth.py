#EXERCICIO-04 crie um documento instanciando uma classe chamada produto, crie a função construtor, com a variável referência que acessa os atributos da classe no espaço alocado de memória.  defina os atributos diretamente na função construtor id, NomeProduto, valor, quantidade crie um segundo documento main com variável referência produto 1, produto 2, produto 3 , insira valores diferentes para cada variável recebendo o objeto, imprima no terminal o espaço  alocado de memória do objeto principal , e de cada variável de referência para o objeto!




class Produto:
    def __init__(self, id, nomeProduto, valor, qtd):
        self.id = id
        self.nomeProduto = nomeProduto
        self.valor = valor
        self.qtd = qtd



produto = Produto('01', 'Dado', 15.5, 35)
produto2 = Produto('02', 'Caixa', 0.25, 80)
produto3 = Produto('03', 'Lapis', 0.35, 23)

print(produto.qtd)
print(produto2.qtd)
print(produto3.qtd)
