
def read_files():
    try:
        with open('contacts.txt', 'r') as file:
            print(file.readlines())
    except FileNotFoundError:
        print('File not found')
    except Exception as error:
        print('Unexpeted error')
        print(error)


def append_files(file_name, line):
    try:
        with open(file_name, 'a') as file:
            file.write(f'{line}\n')
    except FileNotFoundError:
        print('file not found')
    except Exception as error:
        print('Unexpeted error')
        print(error)


def clear_file(file_name):
    try:
        with open(file_name, 'w') as file:
            file.write('')
    except FileNotFoundError:
        print('file not found')
    except Exception as error:
        print('Unexpeted error')
        print(error)