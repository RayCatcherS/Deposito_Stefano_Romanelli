class Persona:
    eta = 0

    # variabile statica, condivisa da tutte le istanze della classe
    stato_civile = "celibe"

    def __init__(self, eta: int):
        self.eta = eta
    def __str__(self):
            return f"Persona con eta {self.eta} e stato civile {self.stato_civile}"

persona1 = Persona(30)

#print(persona1.eta)
#print(Persona.stato_civile) 

print(persona1)