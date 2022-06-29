first_player, second_player = input().split(', ')
size = 6

matrix = []

for row in range(size):
    row_info = input().split(' ')
    matrix.append(row_info)

skip_turns = {
    first_player: 0,
    second_player: 0,
}

turn = 0
current_player = ''

while True:

    command = input().split(', ')

    command_row = int(command[0][1:])
    command_col = int(command[1][:-1])

    if turn % 2 == 0:
        current_player = first_player
    elif turn % 2 != 0:
        current_player = second_player

    if skip_turns[current_player] == 1:
        skip_turns[current_player] = 0
        turn += 1
        continue

    if matrix[command_row][command_col] == 'E':
        print(f"{current_player} found the Exit and wins the game!")
        break
    elif matrix[command_row][command_col] == 'T':
        if current_player == 'Tom':
            print("Tom is out of the game! The winner is Jerry.")
            break
        else:
            print("Jerry is out of the game! The winner is Tom.")
            break
    elif matrix[command_row][command_col] == 'W':
        print(f"{current_player} hits a wall and needs to rest.")
        skip_turns[current_player] += 1

    turn += 1
