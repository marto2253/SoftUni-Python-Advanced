import os

commands = input()

while commands != 'End':

    commands = commands.split('-')

    command = commands[0]
    file_name = commands[1]

    if command == 'Create':
        file = open(file_name, 'w')
        file.write('')
        file.close()
    elif command == 'Add':
        content = commands[2]
        file = open(file_name, 'a')
        file.write(f'{content}\n')
        file.close()
    elif command == 'Replace':
        old_string = commands[2]
        new_string = commands[3]

        try:
            file = open(file_name, 'r+')
            file_content = file.read().replace(old_string, new_string)
            file.seek(0)
            file.truncate(0)
            file.write(file_content)
            file.close()
        except FileNotFoundError:
            print('An error occurred')

    elif command == 'Delete':
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print('An error occurred')

    commands = input()