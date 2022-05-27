

size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(i) for i in input().split()])

while True:
    command = input()

    if command == 'END':
        break

    command = command.split()
    row = int(command[1])
    column = int(command[2])
    value = int(command[3])

    if command[0] == 'Add' and 0 <= row < size and 0 <= column < size:
        matrix[row][column] += value
    elif command[0] == 'Subtract' and 0 <= row < size and 0 <= column < size:
        matrix[row][column] -= value
    else:
        print('Invalid coordinates')

for row in matrix:
    print(*row, sep=' ')
