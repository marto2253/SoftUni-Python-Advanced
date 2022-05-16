from collections import deque


def water_dispenser(water):
    people = deque()
    seq = input()

    while seq != 'Start':
        people.append(seq)
        seq = input()

    seq = input()

    while seq != 'End':
        if seq.startswith('refill'):
            seq = seq.split(' ')
            water += int(seq[1])
        else:
            if int(seq) <= water:
                print(people.popleft(), 'got water')
                water -= int(seq)
            else:
                print(people.popleft(), 'must wait')
        seq = input()
    print(f"{water} liters left")


water_quantity = int(input())
water_dispenser(water_quantity)
