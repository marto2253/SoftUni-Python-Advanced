def balanced(seq):

    stack = []

    pairs = {
        '(': ')',
        '{': '}',
        '[': ']',
    }

    is_balanced = True

    for item in seq:
        if item in '{[(':
            stack.append(item)
        elif not stack:
            is_balanced = False
            break
        else:
            if pairs[stack[-1]] != item:
                is_balanced = False
                break
            else:
                stack.pop()

    if not is_balanced or stack:
        print('NO')
    else:
        print('YES')


sequence = input()
balanced(sequence)
