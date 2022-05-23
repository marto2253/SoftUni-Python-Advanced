from collections import deque


def expression_eval(seq):

    result = ''
    current_seq = ''
    while seq:
        item = seq.popleft()

        if item in '-/+*':
            for i in current_seq:
                result = f'({result} {item} {i})'
                current_seq = ''
        else:
            current_seq += item

    print(eval(result))


sequence = deque(input().split())
expression_eval(sequence)
