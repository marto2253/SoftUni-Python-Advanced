rows, columns = [int(i) for i in input().split(', ')]

matrix = []
for _ in range(rows):
    numbers = [int(i) for i in input().split()]
    matrix.append(numbers)

# print(matrix)

for col in range(columns):
    sum_of_columns = 0
    for row in range(rows):
        # print(matrix[row][col])
        sum_of_columns += matrix[row][col]
    print(sum_of_columns)