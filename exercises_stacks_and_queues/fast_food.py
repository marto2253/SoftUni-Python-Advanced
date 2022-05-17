from collections import deque


def fast_food(food):
    sequence = input()
    sequence = sequence.split()
    queue = deque()

    while sequence:
        item = sequence.pop()
        queue.appendleft(int(item))

    print(max(queue))

    while True:
        order = queue.popleft()
        if order <= food:
            food -= order
            if len(queue) == 0:
                print('Orders complete')
                break
        else:
            queue.appendleft(order)
            print(f'Orders left: {" ".join(str(i) for i in queue)}')
            break


food = int(input())
fast_food(food)
