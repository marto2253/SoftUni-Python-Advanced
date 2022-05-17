def reverse_numbers(seq):
    stack = [i for i in seq.split(' ')]
    reversed_nums = ''
    while stack:
        num = stack.pop()
        reversed_nums += num + ' '

    return reversed_nums


sequenec = input()
print(reverse_numbers(sequenec))
