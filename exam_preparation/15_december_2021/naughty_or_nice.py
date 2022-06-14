
def naughty_or_nice_list(*args, **kwargs):

    kids = {
        'Nice': [],
        'Naughty': [],
        'Not found': [],
    }

    initial_kids_list = args[0]
    commands_first_set = args[1:]
    commands_second_set = kwargs

    for command in commands_first_set:
        command = command.split('-')
        number = int(command[0])
        type = command[1]
        counter = 0
        name = ''
        index = 0
        for kid in range(len(initial_kids_list) -1, -1, -1):
            if number == initial_kids_list[kid][0]:
                index = kid
                name += initial_kids_list[kid][1]
                counter += 1

        if counter == 1:
            initial_kids_list.pop(index)
            kids[type].append(name)

    for k, t in commands_second_set.items():
        counter = 0
        name = ''
        index = 0
        for kid in range(len(initial_kids_list) -1, -1, -1):
            if k == initial_kids_list[kid][1]:
                index = kid
                name += k
                counter += 1
        if counter == 1:
            initial_kids_list.pop(index)
            kids[t].append(k)

    while initial_kids_list:
        popped = initial_kids_list.pop()
        kids['Not found'].append(popped[1])

    result = []

    for k, v in kids.items():
        if len(v) != 0:
            result.append(f'{k}: {", ".join([i for i in v])}')

    return '\n'.join(result)


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print('---------------------------------------------')

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))

print('---------------------------------------------')

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
