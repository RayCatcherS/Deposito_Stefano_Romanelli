import datetime

IN_CONSEGNA = "IN_CONSEGNA"
IN_MAGAZZINO = "IN_MAGAZZINO"
CONSEGNATO = "CONSEGNATO"

class Pacco:
    codice:str = ""
    peso:float = 0.0
    stato:str = IN_MAGAZZINO
    storia:list = []
    def __init__(self, codice:str, peso:float):
        self.codice = codice
        self.peso = peso
        # Aggiungiamo lo storico con la data di creazione e orario di creazione del pacco
        self.storia = [f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Creato in magazzino"]

    @staticmethod
    def ottieni_stati_validi():
        return [IN_CONSEGNA, IN_MAGAZZINO, CONSEGNATO]
      
    def mostra_info(self):
        print(f"Codice: {self.codice}, Peso: {self.peso}, Stato: {self.stato}")
        print("Storia del pacco:")
        for evento in self.storia:
            print(f" - {evento}")
    
    def cambia_stato(self, nuovo_stato:str):
        if nuovo_stato in Pacco.ottieni_stati_validi():
            self.storia.append(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Stato cambiato da {self.stato} a {nuovo_stato}")
            self.stato = nuovo_stato
        else:
            print(f"Errore, stato non valido: {nuovo_stato}")

class GestorePacchi:
    
    # cambia lo stato del pacco da IN_MAGAZZINO a IN_CONSEGNA, errore se il pacco non è in magazzino
    def spedisci_pacco(self, pacco:Pacco):
        if pacco.stato == IN_MAGAZZINO:
            pacco.stato = IN_CONSEGNA
            print(f"Pacco {pacco.codice} spedito.")
        else:
            print(f"Il pacco {pacco.codice} non è in magazzino e non può essere spedito.")
    
    # cambia lo stato del pacco da IN_CONSEGNA a CONSEGNATO, errore se il pacco non è in consegna
    def consegna_pacco(self, pacco:Pacco):
        if pacco.stato == IN_CONSEGNA:
            pacco.stato = CONSEGNATO
            print(f"Pacco {pacco.codice} consegnato.")
        else:
            print(f"Il pacco {pacco.codice} non è in consegna e non può essere consegnato.")

    # calcola il peso totale dei pacchi
    def calcola_peso_tot(self, lista_pacchi:list):
        peso_tot = 0.0
        for pacco in lista_pacchi:
            peso_tot += pacco.peso
        return peso_tot

class Magazzino:
    pacchi: dict = {}
    def __init__(self):
        self.pacchi = {}
    
    gestore_pacchi = GestorePacchi()
    # codice pacco incrementale
    def calcola_codice__nuovo_pacco(self):
        if len(self.pacchi) == 0:
            return "0"
        else:
            return str(int(max(self.pacchi.keys())) + 1)

    # aggiunge un nuovo pacco al magazzino chiedendo all'utente il peso del pacco e calcolando un codice univoco per il pacco
    def aggiungi_pacco(self):
        codice = self.calcola_codice__nuovo_pacco()
        peso = 0.0
        while True:
            peso_input = input("Inserisci il peso del pacco: ")
            try:
                peso = float(peso_input)
                break
            except ValueError:
                print("Peso non valido. Inserisci un numero reale.")
                
        nuovo_pacco = Pacco(codice, peso)
        self.pacchi[codice] = nuovo_pacco

    # cerca un pacco nel magazzino in base al codice e restituisce il pacco trovato o None se non trovato
    def cerca_pacco(self, codice:str):
        return self.pacchi.get(codice, None) # Restituisce il pacco se trovato, altrimenti None
    
    # mostra i pacchi di un inseiem di stati e restituisce la lista dei pacchi filtrati
    def mostra_pacchi_per_stato(self, stati:set):
        pacchi_filtrati = self.filtra_pacchi_per_stato(stati)

        if pacchi_filtrati:
            print(f"Pacchi con stato/i '{stati}':")
            for pacco in pacchi_filtrati:
                pacco.mostra_info()
        else:
            print(f"Nessun pacco trovato con stato/i '{stati}'.")

    def filtra_pacchi_per_stato(self, stato:set):
        pacchi_filtrati = []
        for pacco in self.pacchi.values():
            if pacco.stato in stato:
                pacchi_filtrati.append(pacco)
        return pacchi_filtrati
    
    
            

def main():
    magazzino = Magazzino()

    for i in range(5):
        magazzino.aggiungi_pacco()

    # spedisci 2 pacchi
    magazzino.gestore_pacchi.spedisci_pacco(magazzino.cerca_pacco("0"))
    magazzino.gestore_pacchi.spedisci_pacco(magazzino.cerca_pacco("1"))

    # consegna 1 pacco
    magazzino.gestore_pacchi.consegna_pacco(magazzino.cerca_pacco("0"))

    # mostra in magazzino
    magazzino.mostra_pacchi_per_stato(IN_MAGAZZINO)

    # mostra in consegna
    magazzino.mostra_pacchi_per_stato(IN_CONSEGNA)

    # somma peso totale pacchi non consegnati
    somma_peso_non_consegnati = magazzino.gestore_pacchi.calcola_peso_tot(magazzino.filtra_pacchi_per_stato(IN_MAGAZZINO))
    print("Peso totale pacchi non consegnati:", somma_peso_non_consegnati)

    # visualizza pacchi consegnati
    print("Pacchi spediti e consegnati:")
    magazzino.mostra_pacchi_per_stato({CONSEGNATO, IN_CONSEGNA})

main()