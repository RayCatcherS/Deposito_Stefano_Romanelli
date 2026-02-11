x = 10

print(x)

class pippo():
    __y=10

    def get_y(self):
        return self.__y

p = pippo()

print(p.get_y())



## ESEMPIO 

class Computer:
    def __init__(self):
        self.__processore = "Intel i5" # Attributo privato

    def get_processore(self):
        return self .__processore

    def set_processore(self, processore):
        self .__processore = processore

pc = Computer ()
print(pc.get_processore())
# Accede all'attributo privato tramite il getter
pc.set_processore("AMD Ryzen 5")
# Modifica l'attributo privato tramite il setter
print(pc.get_processore())