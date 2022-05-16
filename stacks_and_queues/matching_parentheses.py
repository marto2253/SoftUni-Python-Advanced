def matching_p(sequence):
    stack = []

    for i in range(len(sequence)):
        if sequence[i] == '(':
            stack.append(i)
        elif sequence[i] == ')':
            start_index = stack.pop()
            print(sequence[start_index:i + 1])


seq = input()
matching_p(seq)