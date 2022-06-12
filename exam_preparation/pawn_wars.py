from string import ascii_lowercase


def capture_black(row, column, matrix):
    if matrix[row][column] == 'w':
        if matrix[row - 1][column - 1] == 'b':
            return True, row - 1, column - 1
        elif matrix[row - 1][column + 1] == 'b':
            return True, row - 1, column + 1


def capture_white(row, column, matrix):
    if matrix[row][column] == 'b':
        if matrix[row + 1][column - 1] == 'w':
            return True, row + 1, column - 1
        elif matrix[row + 1][column + 1] == 'w':
            return True, row + 1, column + 1


def move(row, column, matrix):
    if matrix[row][column] == 'w':
        return row - 1, column
    else:
        return row + 1, column


dd = {
    0: '8',
    1: '7',
    2: '6',
    3: '5',
    4: '4',
    5: '3',
    6: '2',
    7: '1',
}


size = 8

w_p_row, w_p_column = 0, 0
b_p_row, b_p_column = 0, 0

matrix = []

for row in range(size):
    row_elements = input().split()
    for column in range(size):
        if row_elements[column] == 'b':
            b_p_row, b_p_column = row, column
        elif row_elements[column] == 'w':
            w_p_row, w_p_column = row, column
    matrix.append(row_elements)

while True:

    white = capture_black(w_p_row, w_p_column, matrix)

    if white:
        w_p_row = white[1]
        w_p_column = white[2]
        print(f"Game over! White win, capture on {ascii_lowercase[w_p_column]}{dd[w_p_row]}.")
        break

    next_row, next_column = move(w_p_row, w_p_column, matrix)

    if 0 > next_row or 0 > next_column or next_row >= size or next_column >= size:
        print(f"Game over! White pawn is promoted to a queen at {ascii_lowercase[w_p_column]}{dd[w_p_row]}.")
        break
    else:
        matrix[next_row][next_column] = 'w'
        matrix[w_p_row][w_p_column] = '-'
        w_p_row, w_p_column = next_row, next_column

    black = capture_white(b_p_row, b_p_column, matrix)

    if black:
        b_p_row = black[1]
        b_p_column = black[2]
        print(f'Game over! Black win, capture on {ascii_lowercase[b_p_column]}{dd[b_p_row]}.')
        break

    next_row, next_column = move(b_p_row, b_p_column, matrix)

    if 0 > next_row or 0 > next_column or next_row >= size or next_column >= size:
        print(f"Game over! Black pawn is promoted to a queen at {ascii_lowercase[b_p_column]}{dd[b_p_row]}.")
        break
    else:
        matrix[next_row][next_column] = 'b'
        matrix[b_p_row][b_p_column] = '-'
        b_p_row, b_p_column = next_row, next_column

