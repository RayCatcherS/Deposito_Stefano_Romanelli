class Umano():
    def cammina(self):
        print("cammina su piedi")

class Struzzo():
    def cammina(self):
        print("cammina su zampe")

class Auto():
    def corri():
        print("corri")

u = Umano()
s = Struzzo()
a = Auto()

def cammina(elemento: object):
    elemento.cammina()


cammina(u)