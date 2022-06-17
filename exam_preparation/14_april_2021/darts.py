player_one, player_two = input().split(', ')
size = 7
matrix = []

for _ in range(size):
    row_info = input().split()
    matrix.append(row_info)

points = {
    player_one: 501,
    player_two: 501
}

turn = 1
round_number = 0
current_player = ''

while True:

    command = input().replace('(', '').replace(')', '').split(', ')
    points_to_deduct = 0

    if turn % 2 == 0:
        current_player = player_two
    else:
        current_player = player_one
        round_number += 1

    row, column = int(command[0]), int(command[1])

    if 0 > row or 0 > column or column >= size or row >= size:
        continue

    points_to_deduct += (int(matrix[row][0]) + int(matrix[row][6])) + int(matrix[0][column]) + int(matrix[6][column])

    if matrix[row][column] == 'B':
        break
    elif matrix[row][column] == 'D':
        points[current_player] -= points_to_deduct * 2
    elif matrix[row][column] == 'T':
        points[current_player] -= points_to_deduct * 3
    elif matrix[row][column].isdigit():
        points[current_player] -= int(matrix[row][column])

    if points[player_one] <= 0 or points[player_two] <= 0:
        break

    turn += 1

print(f'{current_player} won the game with {round_number} throws!')
