from collections import deque


def paint_colors(seq):

    main_colors = ['red', 'yellow', 'blue']
    secondary_colors = ['orange', 'purple', 'green']

    colors = []

    while seq:
        first_word = seq.popleft()
        last_word = seq.pop() if seq else ''

        result = first_word + last_word
        if result in main_colors or result in secondary_colors:
            colors.append(result)
            continue

        result = last_word + first_word
        if result in main_colors or result in secondary_colors:
            colors.append(result)
            continue

        if first_word:
            seq.insert(len(seq) // 2, first_word[:-1])
        if last_word:
            seq.insert(len(seq) // 2, last_word[:-1])

    result = []

    pairs = {
        'orange': ['yellow', 'red'],
        'purple': ['blue', 'red'],
        'green': ['blue', 'yellow'],
    }

    for color in colors:
        if color in main_colors:
            result.append(color)
        else:
            is_collected = True
            for helper_color in pairs[color]:
                if helper_color not in colors:
                    is_collected = False

            if is_collected:
                result.append(color)

    print(result)


sequence = deque(i for i in input().split())
paint_colors(sequence)
