import repository as repo
import inputs as iu

def menu():
    print("====MENU====")
    print("1) Login")
    print("x) Exit application")

def main():
    while True:
        repo.load_all()
        print(menu())
        choice = input("Please choose functionality: ")
        if choice == '1':       #login
            iu.login()          #vraca poziciju ulogovanog
        elif choice == '2':
            print("Exiting...")
            repo.save_all()
            break
        elif choice == '3':






if __name__=="__main__":
    main()