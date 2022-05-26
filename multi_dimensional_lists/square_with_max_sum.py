import sys

rows, columns = [int(i) for i in input().split(', ')]

matrix = []

for _ in range(rows):
    numbers = [int(i) for i in input().split(', ')]
    matrix.append(numbers)

max_sum = -sys.maxsize
square_matrix = []

for row in range(rows-1):
    for col in range(columns-1):
        submatrix = [matrix[row][col], matrix[row][col+1], matrix[row+1][col], matrix[row+1][col+1]]

        if sum(submatrix) > max_sum:
            max_sum = sum(submatrix)
            square_matrix = submatrix.copy()

print(square_matrix[0], square_matrix[1])
print(square_matrix[2], square_matrix[3])
print(max_sum)
