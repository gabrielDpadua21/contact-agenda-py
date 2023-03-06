try:
    with open('contacts.txt', 'r') as file:
        print(file.readlines())
except FileNotFoundError:
    print('File not found')
