# creare un sistema ripetibile che simuli un teatro
SERVIZI_EXTRA = ["accesso lounge", "servizio in posto", "prenotazione snack"]



# Classe per rappresentare un posto nel teatro
class Posto:
    def __init__(self, numero: int, fila: int):
        self._numero = numero
        self._fila = fila
        self._occupato = False
    
    def prenota(self):
        if self._occupato:
            print("Il posto è già occupato")
        else:
            self._occupato = True

    def libera(self):
        if not self._occupato:
            print("Il posto non è stato prenotato")
        else:
            self._occupato = False

    def get_occupato(self) -> bool:
        return self._occupato
    
    def get_numero(self) -> int:
        return self._numero
    
    def get_fila(self) -> int:
        return self._fila
    
    def info_posto(self) -> str:
        return f" Numero: {self._numero}, Fila {self._fila}, prenotato {self._occupato}"

class PostoVip(Posto):
    servizi = []
    def __init__(self, numero: int, fila: int):
        Posto.__init__(self, numero, fila)
        
    def prenota(self):
        super().prenota()
        servizi = self._seleziona_servizi()

    def _seleziona_servizi(self):
        servizi_selezionati = []

        # seleziona da lista di servizi
        # stampa servizi enumerati
        for i, attributeName in enumerate(SERVIZI_EXTRA):
            print(f"{i} - {attributeName}")

        while True:
            print(f"servizi selezionati: {servizi_selezionati}")
            scelta = input("Inserisci il numero del servizio desiderato (0 per terminare): ")
            if scelta.isdigit():
                scelta = int(scelta)
            
            if scelta == 0:
                break

            if scelta >= 0 and scelta < len(SERVIZI_EXTRA):
                servizi_selezionati.append(SERVIZI_EXTRA[scelta])
            else:
                print("Scelta non valida. Riprova")
        return servizi_selezionati

    def info_posto(self) -> str:
        return super().info_posto()#.join(str(self.servizi))
                

class PostoStandard(Posto):
    def __init__(self, numero: int, fila: int, costo: int):
        Posto.__init__(self, numero, fila)
        self._costo = costo
    
    def get_costo(self) -> int:
        return self._costo
    
    def prenota(self):
        super().prenota()
        print(f"Costo del biglietto: {self.get_costo()} euro")
        
    def info_posto(self) -> str:
        string = super().info_posto() + f" costo: {str(self._costo)}"
        return string
    
class Teatro:
    _lista_posti = []
    def __init__(self):
        pass
    
    def aggiungi_posto(self, posto: Posto):
        self._lista_posti.append(posto)

    def prenota_posto(self, numero: int, fila: int):
        for posto in self._lista_posti:
            if posto.get_numero() == numero and posto.get_fila() == fila:
                posto.prenota()
                break

    def stampa_posti_occupati(self):
        for posto in self._lista_posti:
            if posto.get_stato():
                print(f" Numero: {posto.get_numero()}, Fila {posto.get_fila()}")
    
    def stampa_posti(self):
        for posto in self._lista_posti:
            print(posto.info_posto())
            


# genera posti standard 
teatro = Teatro()

for i in range(4):
    posto = PostoStandard(i+1, 0, 10)
    teatro.aggiungi_posto(posto)

for i in range(2):
    posto = PostoVip(i+1, 1)
    teatro.aggiungi_posto(posto)


teatro.prenota_posto(1,0)
teatro.prenota_posto(1,1)


teatro.stampa_posti()