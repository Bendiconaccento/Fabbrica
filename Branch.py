
import Cioccolato 

class Cioccolatino(Cioccolato):

    def __init__(self, forma, ripieno, tipo, percentuale):

        super().__init__(tipo, percentuale)
        self.forma = forma
        self.ripieno = ripieno

        self.costo_cioccolato = 2

    def produce(self):
        
        super().produce()
        print(f"La forma è: {self.forma}, il ripieno è {self.ripieno}, consuma {self.costo_cioccolato} unità.")


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


class CioccolatoCaldo(Cioccolato):

    def __init__(self, tipo, percentuale, temperatura, densita):

        super().__init__(tipo, percentuale)
        self.temperatura = temperatura
        self.densita = densita

        self.costo_cioccolato = max(20, min(100, self.densita)) 

    def produce(self):

        super().produce()
        print(f"Temperatura: {self.temperatura}°C, Densità: {self.densita}. Consuma {self.costo_cioccolato} unità di cioccolato.")






def main():

    fabbrica = FabbricaCioccolato()

    while True:
        print("\nBenvenuto nella fabbrica di cioccolato!")
        print("1. Produci Cioccolatino")
        print("2. Produci Tavoletta")
        print("3. Produci Cioccolata Calda")
        print("4. Esci")
        
        scelta = input("Scegli un'opzione (1-4): ")

        if scelta == "1":
           
            tipo = input("Inserisci il tipo di cioccolato (fondente, al latte, bianco): ")
            percentuale = int(input("Inserisci la percentuale di cacao: "))
            forma = input("Inserisci la forma del cioccolatino (es. sfera, cubo): ")
            ripieno = input("Inserisci il ripieno del cioccolatino (es. nocciole, mandorle): ")

            cioccolatino = Cioccolatino(forma, ripieno, tipo, percentuale)
            fabbrica.produrre_cioccolato(cioccolatino)

        elif scelta == "2":
           
            tipo = input("Inserisci il tipo di cioccolato (fondente, al latte, bianco): ")
            percentuale = int(input("Inserisci la percentuale di cacao: "))
            peso = int(input("Inserisci il peso della tavoletta (in grammi): "))
            aggiunte = input("Inserisci eventuali aggiunte (es. nocciole, mandorle) o lascia vuoto: ").split(',')

            tavoletta = Tavoletta(peso, tipo, percentuale, aggiunte)
            fabbrica.produrre_cioccolato(tavoletta)

        elif scelta == "3":
           
            tipo = input("Inserisci il tipo di cioccolato (fondente, al latte, bianco): ")
            percentuale = int(input("Inserisci la percentuale di cacao: "))
            temperatura = int(input("Inserisci la temperatura della cioccolata calda (in °C): "))
            densita = int(input("Inserisci la densità della cioccolata calda: "))

            cioccolata_calda = CioccolatoCaldo(tipo, percentuale, temperatura, densita)
            fabbrica.produrre_cioccolato(cioccolata_calda)

        elif scelta == "4":
            print("Grazie per aver utilizzato la fabbrica di cioccolato!")
            break

        else:
            print("Scelta non valida. Riprova.")

main()