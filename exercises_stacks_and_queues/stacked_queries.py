def stacked_queries(num):
    stack = []

    for i in range(num):
        query = input()
        if query.startswith('1'):
            query = query.split()
            stack.append(int(query[1]))
        elif query == '2':
            if len(stack) > 0:
                stack.pop()
        elif query == '3':
            if len(stack) > 0:
                print(max(stack))
        elif query == '4':
            if len(stack) > 0:
                print(min(stack))

    print(', '.join([str(i) for i in reversed(stack)]))


number = int(input())
stacked_queries(number)
