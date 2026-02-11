import random
import time

RUOLO_ATTACCANTE = "attaccante"
RUOLO_DIFENSORE = "difensore"
RUOLO_CENTROCAMPISTA = "centrocampista"

# Mosse
ATTACCA = "attacco"
DIFENDI = "difendi"

class Mossa():
    def __init__(self, tipo_mossa, attacco_mossa: int, difesa_mossa: int):
        self.tipo_mossa = tipo_mossa
        self.attacco_mossa = attacco_mossa
        self.difesa_mossa = difesa_mossa


class MembroSquadra():
    def __init__(self, nome:str, eta:int):
        self.nome = nome
        self.eta = eta

    def descrivi(self):
        return f"{self.nome} - {self.__class__.__name__}"
    
    # polimorfismo genera mossa
    def genera_mossa(self) -> Mossa:
        pass

class Giocatore(MembroSquadra):
    mosse_possibili = [ATTACCA, DIFENDI]

    def __init__(self, nome:str, eta:int, ruolo:str, numero:int, attacco:int, difesa:int):
        super().__init__(nome, eta)
        self.ruolo = ruolo
        self.numero = numero
        self.attacco = attacco
        self.difesa = difesa
    
    # comportamento generazione mossa giocatore
    # il giocatore randomizza l'attacco e la difesa della mossa partendo dalle sue statistiche 
    # il tipo di mossa scelta è casuale
    def genera_mossa(self) -> Mossa:
        # randomizza la mossa ATTACCO O DIFESA
        tipo_mossa = random.choice(self.mosse_possibili)

        # randomizza l'attacco e la difesa della mossa partendo dalle statistiche del giocatore
        attacco_mossa = random.randint(1, self.attacco)
        difesa_mossa = random.randint(1, self.difesa)

        return Mossa(tipo_mossa, attacco_mossa, difesa_mossa)
    
class Allenatore(MembroSquadra):
    def __init__(self, nome:str, eta:int):
        MembroSquadra.__init__(self, nome, eta)
    
    # comportamento generazione mossa giocatore
    # l'allenatore genera la mossa attacco col max
    def genera_mossa(self) -> Mossa:
        return Mossa(ATTACCA, 10, 0)

class Assistente(MembroSquadra):
    def __init__(self, nome:str, eta:int):
        MembroSquadra.__init__(self, nome, eta)

    # comportamento generazione mossa giocatore
    # l'assistente genera la mossa di difesa col max
    def genera_mossa(self) -> Mossa:
        return Mossa(DIFENDI, 0, 10)



class Squadra():
    
    def __init__(self, lista_membri: list):
        self.squadra = lista_membri
    
    def select_giocatore_scontro(self) -> MembroSquadra:
        # seleziona giocatore casuale
        return random.choice(self.squadra)

class Partita():
    def __init__(self, sq1: Squadra, sq2: Squadra, turni):
        self.sq1 = sq1
        self.sq2 = sq2
        self.turni = turni
        self.punti_squadra1 = punti_squadra1 = 0
        self.punti_squadra2 = punti_squadra2 = 0
    
    # gioco principale
    def gioca(self):
        for i in range(self.turni):
            print(f"\n--- TURNO {i+1} ---")
            time.sleep(1) # Wait per l'inizio del turno
            self.__avvia_turno()
            self.print_punteggio_partita()
            time.sleep(1.5) # Wait tra un turno e l'altro

        print("\n=== FISCHIO FINALE ===")
        self.print_punteggio_partita()

    # avvio del turno prevede la selezione di due giocatori casuali dalle due squadre
    # se la mossa del primo giocatore è "difendi" il secondo giocatore "attacca" e viceversa
    def __avvia_turno(self):
        # selezione casuale dei due membre dalle squadre
        membro1 = self.sq1.select_giocatore_scontro()
        membro2 = self.sq2.select_giocatore_scontro() 

        mossa1 = membro1.genera_mossa()
        mossa2 = membro2.genera_mossa()

        # Annuncio della sfida
        print(f"SFIDA: {membro1.descrivi()} (SQ1) e {membro2.descrivi()} (SQ2) si sfidano!")
        self.__next_turn_step()

        # la squadra 1 attacca
        if mossa1.tipo_mossa == ATTACCA:
            print(f"{membro1.descrivi()} (SQ1) lancia un attacco! Attacco: {mossa1.attacco_mossa} su {membro2.descrivi()} con difesa: {mossa2.difesa_mossa}")
            self.__next_turn_step()
            # se la difesa della mossa della squadra 2 < attacco della mossa della squadra 1
            # => squadra 1 segna
            if mossa1.attacco_mossa > mossa2.difesa_mossa:
                # squadra 1 segna
                self.punti_squadra1 = self.punti_squadra1 + 1
                print(f"GOL della Squadra 1! L'attacco: di {membro1.nome} (SQ1) batte la difesa di {membro2.nome} (SQ2)")

            else:
                # squadra 1 non riesce a segnare
                print(f"Difesa impenetrabile! difesa: {membro2.nome} (SQ2) ferma l'attacco di {membro1.nome} (SQ1).")

        elif mossa1.tipo_mossa == DIFENDI:
            print(f"{membro2.descrivi()} (SQ2) lancia un attacco! Attacco: {mossa2.attacco_mossa} su {membro1.descrivi()} con difesa: {mossa1.difesa_mossa}")
            self.__next_turn_step()
            # se la difesa della mossa della squadra 1 < attacco della mossa della squadra 2
            # => squadra 2 segna
            if mossa1.difesa_mossa < mossa2.attacco_mossa:
                # squadra 2 segna
                self.punti_squadra2 = self.punti_squadra2 + 1
                print(f"GOL della Squadra 2! L'attacco di {membro2.nome} (SQ2) batte la difesa di {membro1.nome} (SQ1)")
            else:
                # squadra 2 non riesce a segnare
                print(f"Difesa impenetrabile! difesa: {membro1.nome} (SQ1) ferma l'attacco di {membro2.nome} (SQ2).")
        else:
            print("errore scontro")

    # qualsiasi input fa procedere lo step del turno
    def __next_turn_step(self):
        # premi qualsiasi tasto per lo step successivo
        _= input("")

    def print_punteggio_partita(self):
        print(f"PUNTEGGIO -> Squadra 1: {self.punti_squadra1} | Squadra 2: {self.punti_squadra2}")




def main():
    # squadra 1
    g_sq1 = [
        # difesa
        Giocatore("Giovanni", 22, RUOLO_DIFENSORE, 1, 3, 6),
        Giocatore("giulio", 21, RUOLO_DIFENSORE, 2, 2, 7),

        # centro campo
        Giocatore("Pino", 22, RUOLO_CENTROCAMPISTA, 3, 4, 5),
        Giocatore("Pippo", 22, RUOLO_CENTROCAMPISTA, 4, 5, 4),
        Giocatore("Domenico", 22, RUOLO_CENTROCAMPISTA, 5, 3, 6),

        # attacco
        Giocatore("Ken", 22, RUOLO_ATTACCANTE, 6, 7, 3),
        Giocatore("Vegeta", 22, RUOLO_ATTACCANTE, 7, 8, 2),

        # allenatore
        Allenatore("Giulio", 40),
        # assistente
        Assistente("Andrea", 30)
    ]

    sq1 = Squadra(g_sq1)

    # squadra 2
    g_sq2 = [
        # difesa
        Giocatore("Mauro", 22, RUOLO_DIFENSORE, 1, 3, 6),
        Giocatore("Piero", 21, RUOLO_DIFENSORE, 2, 2, 7),

        # centro campo
        Giocatore("Gianni", 22, RUOLO_CENTROCAMPISTA, 3, 4, 5),
        Giocatore("Luca", 22, RUOLO_CENTROCAMPISTA, 4, 5, 4),
        Giocatore("Angelo", 22, RUOLO_CENTROCAMPISTA, 5, 3, 6),

        # attacco
        Giocatore("Goku", 22, RUOLO_ATTACCANTE, 6, 7, 3),
        Giocatore("Ian", 22, RUOLO_ATTACCANTE, 7, 8, 2)
    ]
    allenatore2 = Allenatore("Pedro", 44)
    assistente2 = Assistente("Pascal", 26)

    sq2 = Squadra(g_sq2)

    # nuova partita
    partita = Partita(sq1, sq2, 10)
    partita.gioca()
main()