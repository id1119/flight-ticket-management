from projekat.menus import (unregistered_menu as unregistered,
                            buyer_menu as buyer)
import projekat.repository as repo

def main():
    logged_username = ''
    status = "unregistered"
    while True:
        if status == 'unregistered':
            logged_username = unregistered.unregistered_menu_main()
            status = repo.users[logged_username]["position"]
            if not status:
                break
        if status == 'buyer':
            status = buyer.buyer_menu_main(logged_username)
            if not status:
                break



if __name__=="__main__":
    main()
