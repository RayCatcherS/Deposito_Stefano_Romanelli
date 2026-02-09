# il metodo di classe è un metodo che dipende dalla classe stessa, non dall'istanza della classe
# viene definito con il decoratore @classmethod
# in questo caso memorizza uno stato nella classe, in questo caso il numero di istanze create

from mimetypes import init


class Contatore:
    numero_istanze = 0 # Attributo di classe

    def __init__(self):
        Contatore.numero_istanze += 1

    @classmethod
    def mostra_numero_istanze(cls):
        print(f"Sono state create {cls.numero_istanze} istanze.")

# Creazione di alcune istanze
c1 = Contatore()
c2 = Contatore()

Contatore.mostra_numero_istanze()
# Output: Sono state create 2 istanze.

# viene possibile accedere all'attributo di classe anche tramite l'istanza, ma è sconsigliato!
print(c1.numero_istanze)
