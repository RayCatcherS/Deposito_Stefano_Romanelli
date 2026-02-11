
class Prova():
    def __init__(self):
        pass

    def __minore(self):
        print("il num è minore")

    def __maggiore(self):
        print("il num è maggiore")

    def check(self, num: int):
        if num < 5:
            self.__minore()
        else:
            self.__maggiore()

prova = Prova()
prova.check(3)
prova.check(7)