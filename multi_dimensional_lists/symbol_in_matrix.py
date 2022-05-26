
n = int(input())

matrix = []

for row in range(n):
    chars = [i for i in input()]
    matrix.append(chars)

# print(matrix)

special_char = input()

found = False

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == special_char:
            result = (row, col)
            print(result)
            found = True
            break
    if found:
        break

if not found:
    print(f'{special_char} does not occur in the matrix')