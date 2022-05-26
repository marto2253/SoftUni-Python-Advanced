from collections import deque
rows, columns = [int(i) for i in input().split()]
word = deque(input())
matrix = []


for i in range(rows):
    ll = list()
    for j in range(columns):
        a = word.popleft()
        ll.append(a)
        word.append(a)

    if i % 2 != 0:
        matrix.append([i for i in reversed(ll)])
    else:
        matrix.append(ll)

for item in matrix:
    print("".join([i for i in item]))



