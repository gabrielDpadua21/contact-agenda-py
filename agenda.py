CONTACTS = {}

def create_contacts():
    name = input("Write the contact name: ")
    phone = input("Write the contact phone: ")
    email = input("Write the contact mail: ")
    try:
        CONTACTS[name] = {
            "tel": phone,
            "mail": email
        }
    except:
        print("Contact already exists...")

def delete_contacts():
    name = input("Write the name of the contact to del: ")
    try:
        CONTACTS.pop(name)
    except:
        print("Contact not exists...")

def clear_contacts():
    CONTACTS.clear()

def list_contacts():
    print(" CONTACTS LIST ")
    for contact in CONTACTS:
        print(contact)

def get_contact_info():
    name = input("Write a name to get contacts info: ")
    try:
        contact = CONTACTS[name]
        print(f"Name: {name}")
        print(f"Phone: {contact['tel']}")
        print(f"E-mail: {contact['mail']}")
    except:
        print("Contact not exists...")

# def exit_contacts():
#     INIT = False

OPTIONS = {
    1: create_contacts,
    2: create_contacts,
    3: clear_contacts,
    4: list_contacts,
    5: get_contact_info
}

if __name__ == "__main__":
    print("Welcome to your list of contacts....")
    while True:
        print("Select one option: ")
        print("1 - create contact")
        print("2 - delete contact")
        print("3 - clear all contacts")
        print("4 - list all contact")
        print("5 - Get Contact Info")
        #print("0 - exit")
        op = int(input())
        try:
            OPTIONS[op]()
        except:
            print("Wrong option, try again!!!")
