
rows, columns = [int(i) for i in input().split()]

matrix = []

for _ in range(rows):
    characters = [i for i in input().split()]
    matrix.append(characters)

# print(matrix)

counter = 0

for row in range(rows - 1):
    for column in range(columns - 1):
        char = {matrix[row][column]}
        square_matrix = {matrix[row][column],matrix[row][column+1], matrix[row+1][column], matrix[row+1][column+1]}
        # print(square_matrix)
        if char == square_matrix:
            counter += 1

print(counter)

