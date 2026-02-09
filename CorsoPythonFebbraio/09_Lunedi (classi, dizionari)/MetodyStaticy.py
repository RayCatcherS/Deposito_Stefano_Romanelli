# metody staticy
# i metodi statici sono metodi che non dipendono dall'istanza della classe, ma dalla classe stessa
# vengono definiti con il decoratore @staticmethod

class Calcolatrice:

    @staticmethod
    def somma(a, b):
        return a + b

# Uso del metodo statico senza creare un'istanza
risultato = Calcolatrice.somma(5, 3)

print(risultato)
# Output: 8