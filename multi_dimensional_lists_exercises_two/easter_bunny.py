def up_direction(bunny, matrix):
    up_moves = []
    up_total = 0

    for i in range(1, size):
        row = int(bunny[0])
        column = int(bunny[1])

        if 0 <= row - i < size and matrix[row - i][column] != 'X':
            up_moves.append([row - i, column])
            up_total += int(matrix[row - i][column])
        else:
            break

    return up_moves, up_total


def down_direction(bunny, matrix):
    down_moves = []
    down_total = 0

    for i in range(1, size):
        row = int(bunny[0])
        column = int(bunny[1])

        if 0 <= row + i < size and matrix[row + i][column] != 'X':
            down_moves.append([row + i, column])
            down_total += int(matrix[row + i][column])
        else:
            break

    return down_moves, down_total


def right_direction(bunny, matrix):
    right_moves = []
    right_total = 0

    for i in range(1, size):
        row = int(bunny[0])
        column = int(bunny[1])

        if 0 <= column + i < size and matrix[row][column + i] != 'X':
            right_moves.append([row, column + i])
            right_total += int(matrix[row][column + i])
        else:
            break

    return right_moves, right_total


def left_direction(bunny, matrix):
    left_moves = []
    left_total = 0

    for i in range(1, size):
        row = int(bunny[0])
        column = int(bunny[1])

        if 0 <= column - i < size and matrix[row][column - i] != 'X':
            left_moves.append([row, column - i])
            left_total += int(matrix[row][column - i])
        else:
            break

    return left_moves, left_total


size = int(input())

matrix = []

for _ in range(size):
    matrix.append([i for i in input().split()])

bunny = ()

for row in range(len(matrix)):
    for column in range(row):
        if matrix[row][column] == 'B':
            bunny += row, column


up = up_direction(bunny, matrix)
down = down_direction(bunny, matrix)
right = right_direction(bunny, matrix)
left = left_direction(bunny, matrix)


result = {
    'up': up,
    'down': down,
    'right': right,
    'left': left,
}

best_score = 0
direction = ''
path = ''

for k, v in result.items():
    if v[1] > best_score and len(v[0]) >= 1:
        best_score = v[1]
        direction = k
        path = v[0]

print(direction)
print(*path, sep='\n')
print(best_score)




