from collections import deque

kids = deque(input().split(' '))
tosses = int(input())

counter = 0
while len(kids) != 1:
    kid = kids.popleft()
    counter += 1
    if counter == tosses:
        print(f'Removed {kid}')
        counter = 0
    else:
        kids.append(kid)

print(f'Last is {kids.popleft()}')


