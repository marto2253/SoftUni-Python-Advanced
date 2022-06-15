size = 6

matrix = []

column_sum = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
}

b_col = []

for row in range(size):
    row_info = input().split()
    for column in range(size):
        if row_info[column] == 'B':
            b_col.append(column)
    matrix.append(row_info)

for row in range(size):
    for column in range(size):
        if matrix[row][column].isdigit():
            column_sum[column] += int(matrix[row][column])

total_points = 0

for _ in range(3):
    command = input().replace('(', '').replace(')', '').split(', ')
    current_row, current_col = int(command[0]), int(command[1])

    if 0 > current_row or 0 > current_col or current_row >= size or current_col >= size:
        continue

    if matrix[current_row][current_col] == 'B':
        total_points += column_sum[current_col]
        matrix[current_row][current_col] = 'x'

if 100 <= total_points < 200:
    print(f"Good job! You scored {total_points} points, and you've won Football.")
elif 200 <= total_points < 300:
    print(f"Good job! You scored {total_points} points, and you've won Teddy Bear.")
elif total_points >= 300:
    print(f"Good job! You scored {total_points} points, and you've won Lego Construction Set.")
else:
    print(f"Sorry! You need {100 - total_points} points more to win a prize.")

