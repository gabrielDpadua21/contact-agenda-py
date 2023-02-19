AGENDA = {}

AGENDA['frajola'] = {
    'tel': '1234',
    'mail': 'frajola@gmail.com',
    'address': 'Av. 1',
}

def list_contacts():
    print("CONTACTS: ")
    print("#####################################")
    for contact in AGENDA:
        print(f"Name: {contact}")
        print(f"Phone: {AGENDA[contact]['tel']}")
        print(f"E-mail: {AGENDA[contact]['mail']}")
        print(f"Address: {AGENDA[contact]['address']}")
        print("#####################################")

def find_contact():
    name = input("Write the contact name: ")
    try:
        contact = AGENDA[name]
        print("#####################################")
        print(f'FIND THE CONTACT: {name}')
        print("#####################################")
        print(f"Name: {name}")
        print(f"Phone: {contact['tel']}")
        print(f"E-mail: {contact['mail']}")
        print(f"Address: {contact['address']}")
    except:
        print("Contact not found")

if __name__ == "__main__":
    print('******* CONTACT AGENDA ******\n')
    find_contact()