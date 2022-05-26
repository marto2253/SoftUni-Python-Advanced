from string import ascii_lowercase
rows, columns = [int(i) for i in input().split()]

matrix = []
for row in range(rows):
    ll = []
    palindrome = ''
    for column in range(columns):
        palindrome += ascii_lowercase[row] + (ascii_lowercase[column+row]) + ascii_lowercase[row]
        ll.append(palindrome)
        palindrome = ''
    matrix.append(ll)


for i in matrix:
    print(" ".join(j for j in i))
