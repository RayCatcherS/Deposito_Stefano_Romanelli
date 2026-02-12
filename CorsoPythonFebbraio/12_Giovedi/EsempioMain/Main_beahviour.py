import Import

# se richiamato nel file di esecuzione principale sarà main
# altrimenti se avviato da un import verrà visto come un import
def check_main():
    if __name__ == "__main__":
        print("main")
    else: 
        print("import")

check_main()

# avviato in un import stamperà che è un import
Import.check_main()