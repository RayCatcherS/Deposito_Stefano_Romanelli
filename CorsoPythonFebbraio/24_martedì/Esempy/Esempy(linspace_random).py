import numpy as np

# --- LINSPACE: Numeri equispaziati ---
# A differenza di arange (dove decidi il PASSO), con linspace decidi QUANTI numeri ottenere.
# Sintassi: np.linspace(inizio, fine, numero_di_elementi)
# NOTA: Qui il valore finale (1) è INCLUSO nel risultato.

arr_lin = np.linspace(0, 1, 5) 
print("Array con linspace (da 0 a 1, 5 elementi):")
print(arr_lin) 
# Output: [0.   0.25 0.5  0.75 1.  ]


# --- RANDOM: Generazione di numeri casuali ---
# Il modulo np.random offre diversi modi per creare dati finti.

# 1. np.random.rand: Valori float tra 0 e 1 (Distribuzione Uniforme)
# Specifichi direttamente la forma (es. 3x3) come argomenti separati
random_float = np.random.rand(3, 3)
print("\nMatrice 3x3 casuale (0-1):")
print(random_float)

# Altre funzioni utili non citate ma comuni:
# np.random.randn(3, 3) -> Distribuzione Normale (media 0, varianza 1)
# np.random.randint(min, max, size) -> Numeri interi casuali