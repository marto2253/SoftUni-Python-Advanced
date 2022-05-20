
def count_values(seq):

    same_values = {}

    for value in seq:
        if value not in same_values:
            same_values[value] = 0
        same_values[value] += 1

    for number, count in same_values.items():
        print(f'{number:.1f} - {count} times')


sequence = [float(i) for i in input().split()]
count_values(sequence)
