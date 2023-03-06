
def read_files():
    try:
        with open('contacts.txt', 'r') as file:
            print(file.readlines())
    except FileNotFoundError:
        print('File not found')
    except Exception as error:
        print('Unexpeted error')
        print(error)


def append_files(name):
    try:
        with open('contacts.txt', 'a') as file:
            file.write(f'{name}\n')
    except FileNotFoundError:
        print('file not found')
    except Exception as error:
        print('Unexpeted error')
        print(error)
