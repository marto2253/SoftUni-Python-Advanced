def fashion(seq):
    capacity = int(input())
    stack = seq.split()
    racks = 1

    current_capacity = capacity

    while stack:
        item = int(stack[-1])
        if item > current_capacity:
            racks += 1
            current_capacity = capacity
        else:
            current_capacity -= item
            stack.pop()
    print(racks)


sequence = input()
fashion(sequence)
