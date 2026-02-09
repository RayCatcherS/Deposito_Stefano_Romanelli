import time

# decoratore per stampare il tempo di esecuzione della funzione
def measure_time(func): 

    def wrapper(*args, **kwargs):
        start_time = time.time()

        # esecuzione funzione wrappata
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time

        print(f"\n[TIME] La funzione '{func.__name__}' ha impiegato {execution_time:.4f} secondi.")

        return result
    return wrapper

# decoratore logger di chiamata, stampa quando una funzione viene avviata
def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"\n[LOG] Avvio funzione: '{func.__name__}'...")
        
        print(f"      args: {args} kwargs: {kwargs}")
        
        result = func(*args, **kwargs)
        
        print(f"[LOG] Fine funzione: '{func.__name__}'.")
        return result
    return wrapper