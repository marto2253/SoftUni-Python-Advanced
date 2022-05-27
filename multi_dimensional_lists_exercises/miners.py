
size = int(input())

commands = [i for i in input().split()]

matrix = []

for _ in range(size):
    sequenece = input().split()
    matrix.append(sequenece)

coal_quantity = 0
collected_coal = 0
start = []
for row in range(size):
    for column in range(size):
        if matrix[row][column] == 's':
            start.append(row)
            start.append(column)
        if matrix[row][column] == 'c':
            coal_quantity += 1

gameOver = False

for command in commands:
    row = int(start[0])
    column = int(start[1])
    if command == 'right':
        if column + 1 <= size - 1:
            start[1] += 1
            updated_matrix = matrix[row][start[1]]
            if updated_matrix == 'c':
                collected_coal += 1
                if coal_quantity == collected_coal:
                    break
                matrix[row][start[1]] = '*'
            elif updated_matrix == 'e':
                print(f'Game over! {start[0], start[1]}')
                gameOver = True
                break
    elif command == 'left':
        if 0 <= column - 1 <= size -1 :
            start[1] -= 1
            updated_matrix = matrix[row][start[1]]
            if updated_matrix == 'c':
                collected_coal += 1
                if coal_quantity == collected_coal:
                    break
                matrix[row][start[1]] = '*'
            elif updated_matrix == 'e':
                print(f'Game over! {start[0], start[1]}')
                gameOver = True
                break
    elif command == 'down':
        if row + 1 <= size -1 :
            start[0] += 1
            updated_matrix = matrix[start[0]][column]
            if updated_matrix == 'c':
                collected_coal += 1
                if coal_quantity == collected_coal:
                    break
                matrix[start[0]][column] = '*'
            elif updated_matrix == 'e':
                print(f'Game over! {start[0], start[1]}')
                gameOver = True
                break
    elif command == 'up':
        if 0 <= row - 1 <= size - 1:
            start[0] -= 1
            updated_matrix = matrix[start[0]][column]
            if updated_matrix == 'c':
                collected_coal += 1
                if coal_quantity == collected_coal:
                    break
                matrix[start[0]][column] = '*'
            elif updated_matrix == 'e':
                print(f'Game over! {start[0], start[1]}')
                gameOver = True
                break

if coal_quantity == collected_coal and not gameOver:
    print(f'You collected all coal! {start[0], start[1]}')
else:
    if not gameOver:
        print(f'{coal_quantity-collected_coal} pieces of coal left. {start[0], start[1]}')

