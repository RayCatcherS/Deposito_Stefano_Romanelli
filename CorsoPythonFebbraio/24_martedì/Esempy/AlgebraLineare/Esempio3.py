import numpy as np

# 1. Creazione del segnale
# Generiamo 400 punti in 1 secondo (frequenza di campionamento = 400Hz)
t = np.linspace(0, 1, 400)

# Il segnale è composto da due onde sinusoidali: una a 50Hz e una a 120Hz
sig = np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 120 * t)

# 2. Calcolo della Trasformata di Fourier (FFT)
# Il risultato è un array di numeri COMPLESSI (con parte reale e immaginaria)
fft_sig = np.fft.fft(sig)

# 3. Calcolo delle frequenze associate
# Serve a mappare i risultati della FFT sulle frequenze reali (Hz)
# Dobbiamo passare la lunghezza del segnale e il passo temporale (d)
freqs = np.fft.fftfreq(len(t), d=(t[1] - t[0]))

print("Primi 5 valori della FFT (numeri complessi):\n", fft_sig[:5])