import numpy as np
import os

def esegui_esercizio():
    while True:
        # 1. Array di 50 numeri equidistanti tra 0 e 10
        array_lin = np.linspace(0, 10, 50)
        
        # 2. Array di 50 numeri casuali tra 0 e 1
        array_rand = np.random.random(50)
        
        # 3. Somma elemento per elemento
        array_somma = array_lin + array_rand
        
        # 4. Somma totale del nuovo array
        somma_totale = np.sum(array_somma)
        
        # 5. Somma degli elementi > 5 (usando Boolean Indexing)
        somma_maggiori_5 = np.sum(array_somma[array_somma > 5])
        
        # 6. Stampa i risultati a video
        print("\n--- RISULTATI ---")
        print(f"Array Linspace (primi 5):\n{array_lin[:5]}")
        print(f"Array Random (primi 5):\n{array_rand[:5]}")
        print(f"Array Somma (primi 5):\n{array_somma[:5]}")
        print(f"Somma Totale: {somma_totale:.2f}")
        print(f"Somma elementi > 5: {somma_maggiori_5:.2f}")

        # 7, 8, 9. Gestione salvataggio su file TXT
        scelta_file = input("\nVuoi sovrascrivere il file TXT? (s/n, invio per 'n'): ").lower()
        modalita = 'w' if scelta_file == 's' else 'a'
        
        with open("risultati_numpy.txt", modalita) as f:
            f.write(f"--- Sessione: {'Sovrascritta' if modalita == 'w' else 'Aggiunta'} ---\n")
            f.write(f"Somma Totale: {somma_totale}\n")
            f.write(f"Somma > 5: {somma_maggiori_5}\n")
            f.write(f"Array Somma completo:\n{array_somma.tolist()}\n\n")
        
        print(f"Dati salvati in 'risultati_numpy.txt' con modalità: {modalita}")

        # Ripetibilità del processo
        ancora = input("\nVuoi eseguire di nuovo il processo? (s/n): ").lower()
        if ancora != 's':
            print("Processo terminato.")
            break

if __name__ == "__main__":
    esegui_esercizio()