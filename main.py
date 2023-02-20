import os


AGENDA = {}


AGENDA["frajola"] = {
    "tel": "1234",
    "mail": "frajola@gmail.com",
    "address": "Av. 1",
}


AGENDA['thor'] = {
    "tel": "54321",
    "mail": "thor@gmail.com",
    "address": "Av. 2"
}


def create_contact():
    name = input("Write the contact name: ")
    phone = input("Write the contact phone: ")
    email = input("Write the contact e-mail: ")
    address = input("Write the contact address: ")
    AGENDA[name] = {
        'tel': phone,
        'mail': email,
        "address": address
    }
    clear()


def list_contacts():
    print("CONTACTS: ")
    print("#####################################")
    for contact in AGENDA:
        show_contact(contact)


def find_contact():
    name = input("Write the contact name: ")
    print("#####################################")
    print(f'FIND THE CONTACT: {name}')
    try:
        show_contact(name)
    except:
        print("Contact not found")


def show_contact(contact):
    print(f"Name: {contact}")
    print(f"Phone: {AGENDA[contact]['tel']}")
    print(f"E-mail: {AGENDA[contact]['mail']}")
    print(f"Address: {AGENDA[contact]['address']}")
    print("#####################################")


def clear():
    os.system("clear")


if __name__ == "__main__":
    print("******* CONTACT AGENDA ******\n")
    create_contact()
    list_contacts()
    find_contact()