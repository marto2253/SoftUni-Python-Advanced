size = 6
rover_row, rover_column = 0, 0

matrix = []

for row in range(size):
    row_elements = input().split()
    for column in range(size):
        if row_elements[column] == 'E':
            rover_row, rover_column = row, column
    matrix.append(row_elements)

directions = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}

commands = input().split(', ')

water = 0
metal = 0
concrete = 0

for command in commands:

    next_row, next_col = directions[command](rover_row, rover_column)

    if 0 > next_row:
        next_row = size - 1
    elif 0 > next_col:
        next_col = size - 1
    elif next_row >= size:
        next_row = 0
    elif next_col >= size:
        next_col = 0

    if matrix[next_row][next_col] == 'R':
        print(f'Rover got broken at {next_row, next_col}')
        break
    elif matrix[next_row][next_col] == 'W':
        print(f'Water deposit found at {next_row, next_col}')
        water += 1
    elif matrix[next_row][next_col] == 'C':
        print(f'Concrete deposit found at {next_row, next_col}')
        concrete += 1
    elif matrix[next_row][next_col] == 'M':
        print(f'Metal deposit found at {next_row, next_col}')
        metal += 1

    rover_row, rover_column = next_row, next_col

if water >= 1 and metal >= 1 and concrete >= 1:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
