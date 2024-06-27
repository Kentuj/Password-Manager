from password_manager.manager import PasswordManager
from colorama import Fore, Style, init
import sys

init(autoreset=True)

def print_menu():
    print(f"\n{Fore.CYAN}{Style.BRIGHT}Password Manager")
    print(f"{Fore.GREEN}1. Aggiungi password")
    print(f"{Fore.YELLOW}2. Recupera password")
    print(f"{Fore.RED}3. Cancella password")
    print(f"{Fore.BLUE}4. Genera password casuale")
    print(f"{Fore.MAGENTA}5. Esci")

def main():
    manager = PasswordManager()

    try:
        while True:
            print_menu()
            choice = input(f"{Fore.WHITE}{Style.BRIGHT}Scegli un'opzione: ")

            if choice == '1':
                service = input(f"{Fore.WHITE}Servizio: ")
                username = input(f"{Fore.WHITE}Username: ")
                password = input(f"{Fore.WHITE}Password: ")
                manager.save_password(service, username, password)
                print(f"{Fore.GREEN}Password salvata con successo.")
            elif choice == '2':
                service = input(f"{Fore.WHITE}Servizio: ")
                result = manager.get_password(service)
                if result:
                    username, password = result
                    print(f"{Fore.GREEN}Username: {username}, Password: {password}")
                else:
                    print(f"{Fore.RED}Servizio non trovato.")
            elif choice == '3':
                service = input(f"{Fore.WHITE}Servizio: ")
                manager.delete_password(service)
                print(f"{Fore.RED}Password cancellata con successo.")
            elif choice == '4':
                length = int(input(f"{Fore.WHITE}Lunghezza password: "))
                print(f"{Fore.GREEN}Password generata: {manager.generate_password(length)}")
            elif choice == '5':
                break
            else:
                print(f"{Fore.RED}Opzione non valida.")

    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Programma interrotto. Arrivederci!")
        sys.exit(0)

if __name__ == '__main__':
    main()