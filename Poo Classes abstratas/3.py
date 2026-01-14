class FormaGeometrica:
    def area(self):
        raise NotImplementedError("Implementa o método area()")
    
def perimetro(self):
    raise NotImplementedError("Implementa o método perimetro()")

class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)
    
    meu_retangulo = Retangulo(10, 5)

print(f"Base: {meu_retangulo.base}, Altura: {meu_retangulo.altura}")
print(f"Área calculada: {meu_retangulo.area()}")
print(f"Perímetro calculado: {meu_retangulo.perimetro()}")