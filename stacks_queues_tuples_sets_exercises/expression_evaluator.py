from collections import deque


def expression_eval(seq):

    result = 0
    current_seq = []
    while seq:
        item = seq.popleft()

        if item in '-/+*':
            pass
        else:
            current_seq.append(int(item))
            current_seq.append('%')

    print(int(result))


sequence = deque(input().split())
expression_eval(sequence)
