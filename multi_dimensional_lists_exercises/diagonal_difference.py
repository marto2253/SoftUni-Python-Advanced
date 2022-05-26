rows = int(input())

matrix = [[int(j)for j in input().split()] for i in range(rows)]
# print(matrix)
diagonal = 0
diagonal_nums = []
secondary_diagonal = 0
second_diagonal_nums = []
for row in range(rows):
    diagonal += matrix[row][row]
    diagonal_nums.append(matrix[row][row])

for row_one in range(rows):
    secondary_diagonal += matrix[row_one][rows-row_one-1]
    second_diagonal_nums.append(matrix[row_one][rows-row_one-1])

print(abs(diagonal - secondary_diagonal))
