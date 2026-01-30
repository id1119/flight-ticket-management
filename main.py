import repository as repo
import inputs as iu
import universal_menu as universal
import copy
import unregistered_menu as unregistered

concrete_flights_copy = {}

def main():
    status = "unregistered"
    while True:
        if status == 'unregistered':
            if not unregistered.unregistered_menu_main():
                break
        # if status == 'registered':



if __name__=="__main__":
    main()
