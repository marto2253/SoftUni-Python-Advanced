

rows = int(input())

matrix = []

for _ in range(rows):
    numbers = [int(i) for i in input().split(', ')]
    matrix.extend(numbers)

print(matrix)