
def paint_colors(seq):

    main_colors = ['red', 'yellow', 'blue']
    secondary_colors = ['orange', 'purple', 'green']

    result = []
    temp = []

    while seq:
        first_item = seq.pop(0)
        if len(seq) != 0:
            last_item = seq.pop()

        if first_item + last_item in main_colors or first_item in main_colors:
            result.append(first_item+last_item)
        elif last_item + first_item in main_colors:
            result.append(last_item + first_item)
        elif first_item + last_item in secondary_colors:
            temp.append(first_item+last_item)
        elif last_item + first_item in secondary_colors:
            temp.append(last_item+first_item)
        else:
            first_item = first_item[0:-1]
            last_item = last_item[0:-1]

            length = len(seq) // 2

            seq.insert(length, first_item+last_item)

        last_item = ''

    print(result)


sequence = input().split()
paint_colors(sequence)
