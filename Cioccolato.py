
class Cioccolato:

    Max = 100

    def __init__(self, tipo, percentuale):

        self.tipo = tipo
        self.percentuale = percentuale

    def produce(self):

        print(f"Il tipo di cioccolato è: {self.tipo}, la percentuale di cacao è {self.percentuale}")


class Cioccolatino(Cioccolato):

    def __init__(self, forma, ripieno, tipo, percentuale):

        super().__init__(tipo, percentuale)
        self.forma = forma
        self.ripieno = ripieno

        self.costo_cioccolato = 2

    def produce(self):
        
        super().produce()
        print(f"La forma è: {self.forma}, il ripieno è {self.ripieno}, consuma {self.costo_cioccolato} unità.")