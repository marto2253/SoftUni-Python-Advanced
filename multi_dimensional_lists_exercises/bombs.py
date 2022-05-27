def get_children(row, column, size):
    possibilities = [
        [row - 1, column - 1],
        [row - 1, column],
        [row - 1, column + 1],
        [row, column - 1],
        [row, column + 1],
        [row + 1, column - 1],
        [row + 1, column],
        [row + 1, column + 1],
    ]

    result = []

    for child_row, child_col in possibilities:
        if 0 <= child_row < size and 0 <= child_col < size and matrix[child_row][child_col] > 0:
            result.append([child_row, child_col])

    return result


size = int(input())
matrix = []

for _ in range(size):
    matrix.append([int(i) for i in input().split()])

commands = input().split()

for command in commands:
    row, column = [int(i) for i in command.split(',')]
    bomb = int(matrix[row][column])

    if bomb > 0:
        children = get_children(row, column, size)
        matrix[row][column] = 0
        for child_row, child_col in children:
            matrix[child_row][child_col] -= bomb

alive_cells = 0
sum_alive_cells = 0

for row in matrix:
    for item in row:
        if item > 0:
            sum_alive_cells += int(item)
            alive_cells += 1

print(f'Alive cells: {alive_cells}')
print(f'Sum: {sum_alive_cells}')

for row in matrix:
    print(*row, sep=' ')
