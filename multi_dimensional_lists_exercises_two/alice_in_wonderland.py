def get_direction(commands, row, col):
    if commands == 'right':
        return row, col + 1
    if commands == 'left':
        return row, col - 1
    if commands == 'up':
        return row - 1, col
    if commands == 'down':
        return row + 1, col

size = int(input())

alice_row = 0
alice_column = 0

matrix = []

for row in range(size):
    row_elements = input().split()
    for column in range(size):
        if row_elements[column] == "A":
            alice_row, alice_column = row, column
    matrix.append(row_elements)


# directions = {
#     'right': lambda r, c: (r, c + 1),
#     'left': lambda r, c: (r, c - 1),
#     'up': lambda r, c: (r - 1, c),
#     'down': lambda r, c: (r + 1, c),
# }

tea_bags_counter = 0
is_failed = False
while tea_bags_counter < 10:
    matrix[alice_row][alice_column] = '*'
    commands = input()
    # next_row, next_col = directions[commands](alice_row, alice_column)
    next_row, next_col = get_direction(commands, alice_row, alice_column)

    if 0 > next_row or 0 > next_col or next_row >= size or next_col >= size:
        break

    alice_row, alice_column = next_row, next_col

    if matrix[alice_row][alice_column] == '.' or matrix[alice_row][alice_column] == '*':
        continue

    if matrix[alice_row][alice_column] == 'R':
        is_failed = True
        break

    tea_bags_counter += int(matrix[alice_row][alice_column])

matrix[alice_row][alice_column] = '*'

if is_failed:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

for row in matrix:
    print(*row, sep=' ')


