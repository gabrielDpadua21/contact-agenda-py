CONTACTS = []

def create_contacts():
    name = input("Write the contact name: ")
    phone = input("Write the contact phone: ")
    contact = {'name': name, 'phone': phone}
    CONTACTS.append(contact)

def delete_contacts():
    list_contacts()
    name = input("Write the name to delete a contact: ")
    for index in range(len(CONTACTS)):
        if CONTACTS[index]['name'] == name:
            del CONTACTS[index]
            break
    list_contacts()

def clear_contacts():
    CONTACTS.clear()

def list_contacts():
    print(" NAME ------------- PHONE")
    for contact in CONTACTS:
        print(f" {contact['name']} ------------- {contact['phone']} ")

if __name__ == "__main__":
    print("Welcome to your list of contacts....")
    while True:
        print("Select one option: ")
        print("1 - create contact")
        print("2 - delete contact")
        print("3 - clear all contacts")
        print("4 - list all contact")
        print("0 - exit")
        op = int(input())
        if op == 0:
            print("Bye")
            break
        elif op == 1:
            create_contacts()
        elif op == 2:
            delete_contacts()
        elif op == 3:
            clear_contacts()
        elif op == 4:
            list_contacts()
        else:
            print("Wrong Option, try again!!!")

