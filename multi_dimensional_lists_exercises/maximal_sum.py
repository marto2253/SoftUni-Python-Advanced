import sys

rows, columns = [int(i) for i in input().split()]

matrix = []

for _ in range(rows):
    numbers = [int(i) for i in input().split()]
    matrix.append(numbers)

# print(matrix)

max_sum = -sys.maxsize
max_rectangle_matrix = []
for row in range(rows - 2):
    for column in range(columns - 2):
        rectangle_matrix = [
            matrix[row][column], matrix[row][column+1], matrix[row][column+2],
            matrix[row+1][column], matrix[row+1][column+1], matrix[row+1][column+2],
            matrix[row+2][column], matrix[row+2][column+1], matrix[row+2][column+2],

        ]
        if sum(rectangle_matrix) > max_sum:
            max_sum = sum(rectangle_matrix)
            max_rectangle_matrix = rectangle_matrix.copy()

print(f'Sum = {max_sum}')
print(max_rectangle_matrix[0], max_rectangle_matrix[1], max_rectangle_matrix[2])
print(max_rectangle_matrix[3], max_rectangle_matrix[4], max_rectangle_matrix[5])
print(max_rectangle_matrix[6], max_rectangle_matrix[7], max_rectangle_matrix[8])

