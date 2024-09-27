
class Cioccolato:

    Max = 100

    def __init__(self, tipo, percentuale):

        self.tipo = tipo
        self.percentuale = percentuale

    def produce(self):

        print(f"Il tipo di cioccolato è: {self.tipo}, la percentuale di cacao è {self.percentuale}")



class Tavoletta(Cioccolato):

    def __init__ (self, peso, tipo, percentuale, aggiunte=None ):

        super().__init__(tipo, percentuale)
        self.peso = peso
        self.aggiunte = aggiunte or []

        self.costo_cioccolato = max(4, min(24, peso // 10))

    def produce(self):

        super().produce()
        aggiunte_descrizione = ",".join(self.aggiunte) if self.aggiunte else "nessuna aggiunta"
        print(f"Il peso è: {self.peso}g, Con aggiunta di: {aggiunte_descrizione}. Consuma {self.costo_cioccolato} unità di cioccolato.")

class Cioccolatino(Cioccolato):

    def __init__(self, forma, ripieno, tipo, percentuale):

        super().__init__(tipo, percentuale)
        self.forma = forma
        self.ripieno = ripieno

        self.costo_cioccolato = 2

    def produce(self):
        
        super().produce()
        print(f"La forma è: {self.forma}, il ripieno è {self.ripieno}, consuma {self.costo_cioccolato} unità.")

