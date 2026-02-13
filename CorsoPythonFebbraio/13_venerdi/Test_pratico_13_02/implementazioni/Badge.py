# Incapsulamento: il badge sarà incapsulato in modo che non possa essere modificato direttamente
class Badge:
    def __init__(self, codice: int, ruolo: str):
        self.__codice = codice          
        self.__ruolo = ruolo

    def get_ruolo(self) -> str:
        return self.__ruolo

    def get_id(self) -> int: 
        return self.__codice