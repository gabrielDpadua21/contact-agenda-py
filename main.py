AGENDA = {}
MENU = {}


AGENDA["frajola"] = {
    "tel": "1234",
    "mail": "frajola@gmail.com",
    "address": "Av. 1",
}


AGENDA["thor"] = {
    "tel": "54321",
    "mail": "thor@gmail.com",
    "address": "Av. 2"
}


def create_contact():
    name = input("Write the contact name: ")
    phone = input("Write the contact phone: ")
    email = input("Write the contact e-mail: ")
    address = input("Write the contact address: ")
    set_contact_infos(name, phone, email, address)
    print('-----------------------------------------')
    print(f"Contact: {name} - register success!!!")
    print('----------------------------------------')


def update_contact():
    try:
        name = input("Write the contact name: ")
        AGENDA[name]
        phone = input("Write the contact phone: ")
        email = input("Write the contact e-mail: ")
        address = input("Write the contact address: ")
        set_contact_infos(name, phone, email, address)
        print('-----------------------------------------')
        print(f"Contact: {name} - update success")
        print('----------------------------------------')
    except KeyError:
        print("Contact not found to delete")
    except Exception as error:
        print(f'Unexpeted error {error}')


def delete_contact():
     name = input("Write the contact name: ")
     try:
        del AGENDA[name]
     except KeyError:
        print("Contact not found to delete")
     except Exception as error:
        print(f'Unexpeted error {error}')


def set_contact_infos(name, phone, email, address):
    AGENDA[name] = {
        'tel': phone,
        'mail': email,
        "address": address
    }


def list_contacts():
    print('CONTACTS: ')
    print('------------------------------------')
    for contact in AGENDA:
        show_contact(contact)
    print('------------------------------------')


def find_contact():
    name = input('Write the contact name: ')
    print('------------------------------------------')
    print(f'FIND THE CONTACT: {name}')
    print('------------------------------------------')
    try:
        show_contact(name)
    except:
        print('Contact not found')


def show_contact(contact):
    print('---------------------------------------')
    print(f'Name: {contact}')
    print(f"Phone: {AGENDA[contact]['tel']}")
    print(f"E-mail: {AGENDA[contact]['mail']}")
    print(f"Address: {AGENDA[contact]['address']}")
    print('---------------------------------------')



MENU = {
    1: create_contact,
    2: update_contact,
    3: list_contacts,
    4: delete_contact,
    5: find_contact
}

def menu_options():
    print(" 1 - CREATE CONTACT")
    print(" 2 - UPDATE CONTACT")
    print(" 3 - LIST ALL CONTACTS")
    print(" 4 - DELETE CONTACT")
    print(" 5 - FIND A CONTACT")
    print(" 6 - EXIT")


def menu():
    menu_options()
    menu_state = True
    try:
        option = int(input("Select one option: "))
        if option == 6:
            menu_state = False
        else:
            MENU[option]()
    except ValueError:
        print("Wrong options, please type only numbers!!!")
    except Exception as error:
        print(f'Unexpeted error {error}')
    return menu_state


if __name__ == "__main__":
    print("******* CONTACT AGENDA ******\n")
    loop = True
    while loop:
        loop = menu()
    else:
        print("Bye")