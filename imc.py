class IMC:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura

    def calculaIMC(self):
        print(self.peso / (self.altura ** 2))

p1 = IMC(65, 1.55)
p1.calculaIMC()