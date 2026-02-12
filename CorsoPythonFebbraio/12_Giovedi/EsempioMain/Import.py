# se richiamato nel file di esecuzione principale sarà main
# altrimenti se avviato da un import verrà visto come un import
def check_main():
    if __name__ == "__main__":
        print("main")
    else: 
        print("import")