def reverse_numbers(seq):
    stack = seq.split(' ')
    reversed_nums = ''
    while stack:
        num = stack.pop()
        reversed_nums += num + ' '

    return reversed_nums


sequenec = input()
print(reverse_numbers(sequenec))
