from collections import deque


def supermarket(seq):
    queue = deque()

    while seq != 'End':
        if seq == 'Paid':
            while queue:
                print(queue.popleft())
        else:
            queue.append(seq)

        seq = input()

    print(len(queue), 'people remaining.')


sequence = input()
supermarket(sequence)
