
rows, columns = [int(i) for i in input().split()]

matrix = []

for row in range(rows):
    expression = [i for i in input().split()]
    matrix.append(expression)

command = input()
while command != 'END':
    command = command.split()

    if command[0] == 'swap':
        first = int(command[1])
        second = int(command[2])
        third = int(command[3])
        fourth = int(command[4])

        if first in range(rows) and second in range(rows) and third in range(rows) and fourth in range(rows) and \
            first in range(columns) and second in range(columns) and third in range(columns) and fourth in range(columns):
            matrix[first][second], matrix[third][fourth] = matrix[third][fourth], matrix[first][second]

            for row in matrix:
                print(*row, sep=' ')
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')

    command = input()

# print(matrix[0])