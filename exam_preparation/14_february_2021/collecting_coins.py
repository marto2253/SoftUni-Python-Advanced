from math import floor

size = int(input())

matrix = []

start_row, start_col = 0, 0

for row in range(size):
    row_info = input().split()
    for column in range(size):
        if row_info[column] == 'P':
            start_row, start_col = row, column
    matrix.append(row_info)

directions = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
}

coins = 0
is_won = False
path = []

while True:

    path.append([start_row, start_col])

    command = input()

    c_row, c_col = directions[command](start_row, start_col)

    if 0 > c_row:
        c_row = size - 1
    elif 0 > c_col:
        c_col = size - 1
    elif c_row >= size:
        c_row = 0
    elif c_col >= size:
        c_col = 0

    if matrix[c_row][c_col] == 'X':
        path.append([c_row, c_col])
        break
    elif matrix[c_row][c_col].isdigit():
        coins += int(matrix[c_row][c_col])

    if coins >= 100:
        is_won = True
        path.append([c_row, c_col])
        break

    matrix[start_row][start_col] = '0'
    start_row, start_col = c_row, c_col

if is_won:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {floor(coins / 2)} coins.")

joining_path = "\n".join([str(i) for i in path])

print(f'Your path:\n{joining_path}')