from controler import Animal

'''animal = Animal('Ocktaman', 'Anfibio', 15, 'Vermelho')
animal2 = Animal('Ovonario', 'Passifero', 25, 'Preto')
animal3 = Animal('Pelendacto', 'Dinauro', 35, 'Roxo')

print(animal.cor)
print(animal2.cor)
print(animal3.cor)
'''
animal = Animal(input('Insira a especie: '), input('Insira o genero: '), int(input('Insira a idade: ')), input('Insira a cor: '))

animal2 = Animal(input('Insira a especie: '), input('Insira o genero: '), int(input('Insira a idade: ')), input('Insira a cor: '))

animal3 = Animal(input('Insira a especie: '), input('Insira o genero: '), int(input('Insira a idade: ')), input('Insira a cor: '))

print(animal.cor)
print(animal2.cor)
print(animal3.cor)