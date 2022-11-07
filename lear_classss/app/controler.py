
infoUser = [18, "Branco", "05686515964"]

class Person:
    def __init__(self, firstName, lastName, proprietiesBuy, carsBuy, patrimony, infoUser):
        self.firstName = firstName
        self.lastName = lastName
        self.proprietiesBuy = proprietiesBuy
        self.carsBuy = carsBuy
        self.patrimony = patrimony
        self.infoUser = infoUser


p1 = Person('Carlos', 'Alberto', 15, 5, 120000000.00, infoUser)

print(p1.lastName)
print(p1.patrimony)
print(p1.infoUser)

        
