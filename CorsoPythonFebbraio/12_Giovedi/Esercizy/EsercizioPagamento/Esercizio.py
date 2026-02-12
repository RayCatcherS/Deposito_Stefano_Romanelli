from abc import ABC, abstractmethod

class MetodoPagamento(ABC):
    @abstractmethod 
    def effettua_pagamento(self, importo: int) -> bool:
        pass

    def pagamento_effettuato(self):
        print("pagamento effettuato")

class CartaDiCredito(MetodoPagamento):
    def effettua_pagamento(self, importo: int) -> bool:
        code = input("inserisci codice carta")
        super().pagamento_effettuato()

class PayPal(MetodoPagamento):
    def effettua_pagamento(self, importo: int) -> bool:
        print("collegamento al servizio paypal")
        super().pagamento_effettuato()

class BonificoBancario(MetodoPagamento):
    def effettua_pagamento(self, importo: int) -> bool:
        print("collegamento al bonifico")
        super().pagamento_effettuato()


def gestore_pagamenti(metodo: MetodoPagamento, importo):
    metodo.effettua_pagamento(importo)



importo = int(input("seleziona importo"))
scelta = input("seleziona pagamento: 1 carta, 2 paypal, 3 banca")

if scelta == "1":
    gestore_pagamenti(CartaDiCredito(), importo)
elif scelta == "2":
    gestore_pagamenti(PayPal(), importo)
elif scelta == "3":
    gestore_pagamenti(BonificoBancario(), importo)
else:
    print("nessun metodo selezionato")