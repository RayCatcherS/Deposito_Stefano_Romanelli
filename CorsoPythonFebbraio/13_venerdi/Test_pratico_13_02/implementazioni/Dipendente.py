from implementazioni.Accesso import Accesso
from astratte.Persona import Persona
from implementazioni.Badge import Badge


# ereditarietà, eredita dalla classe astratta Persona metodi (da implementare) e attributi 
class Dipendente(Persona):

    def __init__(self, nome: str, cognome: str, badge: Badge):
        super().__init__(nome, cognome) # chiamata al costruttore della classe padre (Persona)
        # init delle variabili private per la classe Dipenedente
        self.__badge = badge # incapsulamento di badge anche privato

    # polimorfismo metodo con comportamento specifico per la classe Dipendente
    def get_accesso(self) -> Accesso:
        self.__badge.get_ruolo()
        accesso = Accesso(badge=self.__badge, ruolo = self.__badge.get_ruolo())
        return accesso