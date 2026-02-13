from implementazioni.Badge import Badge


class Accesso:

    def __init__(self, badge: Badge = None, ruolo = None):
        self.__badge = badge
        self.__ruolo = ruolo

    def get_badge(self) -> Badge:
        return self.__badge
    
    def get_ruolo(self) -> str:
        return self.__ruolo

