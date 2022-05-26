

rows, columns = [int(i) for i in input().split(', ')]

matrix = []
sum_of_numbers = 0
for row in range(rows):
    numbers = [int(i) for i in input().split(', ')]
    sum_of_numbers += sum(numbers)
    matrix.append(numbers)

print(sum_of_numbers)
print(matrix)