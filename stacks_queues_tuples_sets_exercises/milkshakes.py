from collections import deque


def milkshakes(chocalates, milk):

    counter = 0

    while True:

        if counter == 5 or len(chocalates) == 0 or len(milk) == 0:
            break

        last_chock = chocalates[-1]
        first_milk_shake = milk[0]

        if last_chock <= 0 and first_milk_shake <= 0:
            chocalates.pop()
            milk.popleft()
            continue
        elif last_chock <= 0:
            chocalates.pop()
            continue
        elif first_milk_shake <= 0:
            milk.popleft()
            continue

        if last_chock == first_milk_shake:
            counter += 1
            chocalates.pop()
            milk.popleft()
        else:
            milk.append(milk.popleft())
            chocalates[-1] -= 5

    if counter == 5:
        print("Great! You made all the chocolate milkshakes needed!")
    else:
        print("Not enough milkshakes.")

    if len(chocalates) != 0:
        print(f"Chocolate: {', '.join([str(i) for i in chocalates])}")
    else:
        print("Chocolate: empty")

    if len(milk) != 0:
        print(f"Milk: {', '.join([str(i) for i in milk])}")
    else:
        print("Milk: empty")


f_input = [int(i) for i in input().split(', ')]
s_input = deque(int(i) for i in input().split(', '))

milkshakes(f_input, s_input)
