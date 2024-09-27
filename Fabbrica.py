import Cioccolato

class FabbricaCioccolato:

    def __init__(self):
        self.quantita_prodotta = 0

    def produrre_cioccolato(self, prodotto):

        if self.quantita_prodotta + prodotto.costo_cioccolato <= Cioccolato.Max:
            prodotto.produce()
            self.quantita_prodotta += prodotto.costo_cioccolato
            print(f"Totale cioccolato prodotto oggi: {self.quantita_prodotta}/{Cioccolato.Max} unità.")
        else:
            print("Limite giornaliero di produzione raggiunto!")
            self.resoconto()
            self.chiedi_continuazione()

    def resoconto(self):
        print(f"Produzione totale giornaliera: {self.quantita_prodotta} unità di cioccolato.")

    def chiedi_continuazione(self):
        risposta = input("Vuoi continuare la produzione domani? (s/n): ").lower()
        if risposta == 's':
            self.quantita_prodotta = 0
            print("Produzione riprenderà domani.")
        else:
            print("Produzione terminata per oggi.")