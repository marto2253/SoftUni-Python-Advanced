from collections import deque


def cups_and_bottles(cups, bottles):
    cups_que = deque([int(i) for i in cups.split()])
    bottles_stack = [int(i) for i in bottles.split()]
    wasted = 0

    while bottles_stack and cups_que:
        bottle = bottles_stack.pop()
        if cups_que[0] - bottle <= 0:
            wasted += abs(cups_que[0] - bottle)
            cups_que.popleft()
        else:
            cups_que[0] = cups_que[0] - bottle

    if len(cups_que) == 0:
        print(f"Bottles: {' '.join([str(i) for i in reversed(bottles_stack)])}")
    else:
        print(f"Cups: {' '.join([str(i) for i in cups_que])}")
    print(f"Wasted litters of water: {wasted}")


cups = input()
bottles = input()
cups_and_bottles(cups, bottles)