from abc import ABC, abstractmethod

class Persona(ABC):

    def __init__(self, nome: str, cognome: str):
        # incapsulamento, utilizzo di variabili protette
        self._nome = nome
        self._cognome = cognome

    def nome_completo(self) -> str:
        # incapsulamento, utilizzo di metodi per accedere alle variabili protette
        return f"{self._nome} {self._cognome}"
    
    @abstractmethod
    def get_ruolo(self) -> str:
        # polimorfismo, tutte le sotto classi devono implementare questo metodo
        # restituendo il ruolo
        # esempio developer, ai developer
        pass

    @abstractmethod
    def accedi_lavoro(self) -> bool:
        # polimorfismo, classe per implementare la logica di accesso al lavoro
        # ogni sotto classe avrà un suo tipo di accesso (badge, ecc)
        pass