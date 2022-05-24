from collections import deque


def expression_eval(seq):

    numbers = deque()

    for ch in seq:
        if ch in '-+/*':
            while len(numbers) > 1:
                left = numbers.popleft()
                right = numbers.popleft()

                if ch == '/':
                    result = eval(f'{left} {"//"} {right}')
                else:
                    result = eval(f'{left} {ch} {right}')

                numbers.appendleft(result)
        else:
            numbers.append(ch)

    print(numbers.popleft())


sequence = input().split()
expression_eval(sequence)
