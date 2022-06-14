rows, columns = [int(i) for i in input().split(', ')]

row_pos, col_pos = 0, 0
matrix = []

collectables = {
    'D': 0,
    'C': 0,
    'G': 0
}

for row in range(rows):
    rows_info = input().split()
    for column in range(columns):
        if rows_info[column] == 'Y':
            row_pos, col_pos = row, column
        elif rows_info[column] == 'D':
            collectables['D'] += 1
        elif rows_info[column] == 'C':
            collectables['C'] += 1
        elif rows_info[column] == 'G':
            collectables['G'] += 1

    matrix.append(rows_info)


def directions(direction):
    if direction == 'right':
        return row_pos, col_pos + 1
    elif direction == 'left':
        return row_pos, col_pos - 1
    elif direction == 'up':
        return row_pos - 1, col_pos
    elif direction == 'down':
        return row_pos + 1, col_pos


is_collected = False
decorations = 0
cookies = 0
gifts = 0
while True:

    commands = input()

    if commands == 'End':
        break

    commands = commands.split('-')

    direction = commands[0]
    steps = int(commands[1])

    for step in range(steps):
        cur_row, cur_col = directions(direction)

        if 0 > cur_row:
            cur_row = rows - 1
        elif 0 > cur_col:
            cur_col = columns - 1
        elif cur_row >= rows:
            cur_row = 0
        elif cur_col >= columns:
            cur_col = 0

        if matrix[cur_row][cur_col] == 'D':
            decorations += 1
        elif matrix[cur_row][cur_col] == 'G':
            gifts += 1
        elif matrix[cur_row][cur_col] == 'C':
            cookies += 1

        matrix[row_pos][col_pos] = 'x'
        matrix[cur_row][cur_col] = 'Y'

        if collectables['G'] <= gifts and collectables['D'] <= decorations and collectables['C'] <= cookies:
            is_collected = True
            break

        row_pos, col_pos = cur_row, cur_col

    if is_collected:
        break

if is_collected:
    print("Merry Christmas!")

print("You've collected:")
print(f"- {decorations} Christmas decorations")
print(f"- {gifts} Gifts")
print(f"- {cookies} Cookies")

print('\n'.join(' '.join(i) for i in matrix))


