
n = int(input())

matrix = []

for _ in range(n):
    numbers = [int(i) for i in input().split()]
    matrix.append(numbers)

diagonal = 0
for row in range(n):
    diagonal += matrix[row][row]
# for row in range(n):
#     for col in range(n):
#         if row == col:
#             diagonal += matrix[row][col]

print(diagonal)