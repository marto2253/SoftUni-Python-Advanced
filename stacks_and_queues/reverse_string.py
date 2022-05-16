def reverse_string(seq):
    stack = [i for i in seq]
    reversed_elements = ''

    while stack:
        reversed_elements += stack.pop()

    return reversed_elements

sequence = input()
print(reverse_string(sequence))