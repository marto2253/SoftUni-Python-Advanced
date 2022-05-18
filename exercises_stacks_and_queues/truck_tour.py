from collections import deque


def truck_tour(num):

    queue = deque()

    for _ in range(num):
        queue.append([int(i) for i in input().split()])

    for attempt in range(num):
        trunk = 0
        failed = False
        for petrol, length in queue:
            trunk = trunk + petrol - length
            if trunk < 0:
                failed = True
                break

        if failed:
            queue.append(queue.popleft())
        else:
            print(attempt)
            break


number = int(input())
truck_tour(number)
