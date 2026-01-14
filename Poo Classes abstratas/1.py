class Animal:
    def __init__(self):
        if type(self) is Animal:
            raise TypeError("abstrata")

    def falar(self):
        raise NotImplementedError("falar().")

class Cachorro(Animal):
    def falar(self):
        return "Au Au!"

class Gato(Animal):
    def falar(self):
        return "Miau!"


dog = Cachorro()
cat = Gato()

print(f"O cachorro diz: {dog.falar()}")
print(f"O gato diz: {cat.falar()}")