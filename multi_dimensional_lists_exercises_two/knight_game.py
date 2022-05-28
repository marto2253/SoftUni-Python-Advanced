def get_count(size, row, column, matrix):
    possibilities = [
        [row - 2, column - 1],
        [row - 2, column + 1],
        [row - 1, column - 2],
        [row + 1, column - 2],
        [row + 2, column - 1],
        [row + 2, column + 1],
        [row - 1, column + 2],
        [row + 1, column + 2],
    ]

    result = 0

    for child_row, child_col in possibilities:
        if 0 <= child_row < size and 0 <= child_col < size and matrix[child_row][child_col] == 'K':
            result += 1

    return result

size = int(input())

matrix = []

for _ in range(size):
    matrix.append([i for i in input()])

removed_knights = 0

while True:
    best_count = 0
    knight_row = 0
    knight_col = 0
    for row in range(len(matrix)):
        for column in range(len(matrix)):
            if matrix[row][column] == '0':
                continue
            count = get_count(size, row, column, matrix)
            if count > best_count:
                best_count = count
                knight_row = row
                knight_col = column

    if best_count > 0:
        matrix[knight_row][knight_col] = '0'
        removed_knights += 1
    else:
        break

print(removed_knights)







