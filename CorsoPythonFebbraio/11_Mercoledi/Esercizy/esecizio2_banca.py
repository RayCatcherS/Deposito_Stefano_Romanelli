class ContoBancario:
    def __init__(self, titolare: str, saldo_iniziale: float = 0.0):
        # Usiamo il setter per validare il nome già alla creazione
        self.titolare = titolare 
        
        # Inizializziamo il saldo (assicurandoci che non sia negativo)
        self._saldo = saldo_iniziale if saldo_iniziale >= 0 else 0.0

    # --- GETTER E SETTER PER IL TITOLARE ---
    
    @property
    def titolare(self):
        """Restituisce il nome del titolare."""
        return self._titolare

    # questo decoratore serve a creare il setter e a fare i controlli
    @titolare.setter
    def titolare(self, nuovo_nome):
        """Valida che il nome sia una stringa e non sia vuota."""
        if isinstance(nuovo_nome, str) and nuovo_nome.strip():
            self._titolare = nuovo_nome
        else:
            print("ERRORE: Il titolare deve essere una stringa non vuota.")

    # --- METODI PER IL SALDO ---

    def visualizza_saldo(self):
        """Accesso in sola lettura al saldo corrente."""
        return self._saldo

    def deposita(self, importo: float):
        """Aggiunge fondi solo se l'importo è positivo."""
        if importo > 0:
            self._saldo += importo
            print(f"Deposito di {importo}€ effettuato con successo.")
        else:
            print(f"ERRORE: Impossibile depositare {importo}€. L'importo deve essere positivo.")

    def preleva(self, importo: float):
        """Sottrae fondi solo se disponibili e l'importo è valido."""
        if importo <= 0:
            print("ERRORE: L'importo del prelievo deve essere positivo.")
        elif importo > self._saldo:
            print(f"ERRORE: Fondi insufficienti. Saldo disponibile: {self._saldo}€.")
        else:
            self._saldo -= importo
            print(f"Prelievo di {importo}€ effettuato. Nuovo saldo: {self._saldo}€.")

# --- ESEMPIO DI UTILIZZO ---

# 1. Creazione conto
mio_conto = ContoBancario("Stefano", 100.0)

# 2. Test depositi e prelievi
mio_conto.deposita(50)      # OK
mio_conto.preleva(200)      # Errore: Fondi insufficienti
mio_conto.preleva(-10)      # Errore: Importo negativo

# 3. Test Getter/Setter titolare
mio_conto.titolare = ""     # Errore: Stringa vuota
print(f"Titolare attuale: {mio_conto.titolare}")

# 4. Tentativo di accesso diretto (Sconsigliato, ma Python non lo impedisce del tutto)
# L'uso del prefisso '_' avvisa gli altri programmatori: "Non toccare questo valore direttamente!"
print(f"Saldo finale visualizzato correttamente: {mio_conto.visualizza_saldo()}€")