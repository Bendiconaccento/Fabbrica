
class Cioccolato:

    Max = 100

    def __init__(self, tipo, percentuale):

        self.tipo = tipo
        self.percentuale = percentuale

    def produce(self):

        print(f"Il tipo di cioccolato è: {self.tipo}, la percentuale di cacao è {self.percentuale}")


