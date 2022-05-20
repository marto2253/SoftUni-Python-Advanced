
def summation_pairs(seq, target):

    counter = 0
    unique_pairs = []
    starting_index = 0
    for num in seq:
        starting_index += 1
        for pair in seq[starting_index:]:
            counter += 1
            if int(num) + int(pair) == target:
                print(f'{num} + {pair} = {target}')
                unique_pair = (int(num), int(pair))
                if unique_pair not in unique_pairs:
                    unique_pairs.append(unique_pair)

    print(f'Iterations done: {counter}')
    [print(i) for i in unique_pairs]


sequnece = input().split()
target_num = int(input())

summation_pairs(sequnece, target_num)
