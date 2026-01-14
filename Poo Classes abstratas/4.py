class Transporte:
    def __init__(self):
        if type(self) is Transporte:
            raise TypeError("A classe é abstrata.")

    def mover(self):
        raise NotImplementedError("mover().")

    def parar(self):
        raise NotImplementedError("parar().")

class Carro(Transporte):
    def mover(self):
        print("O carro está acelerando.")

    def parar(self):
        print("O carro freou e parou.")

meu_carro = Carro()
meu_carro.mover()
meu_carro.parar()