from collections import deque


def honey(bees, nectar, symbols):

    total = 0

    while len(nectar) != 0 and len(bees) != 0:
        first_bee = bees[0]
        last_nectar = nectar[-1]

        if last_nectar >= first_bee:
            symbol = symbols.popleft()
            total += abs(eval(f'{first_bee} {symbol} {last_nectar}'))
            bees.popleft()
            nectar.pop()
        else:
            nectar.pop()

    print(f'Total honey made: {total}')
    if len(bees) != 0:
        print(f"Bees left: {', '.join([str(i) for i in bees])}")
    if len(nectar) != 0:
        print(f"Nectar left: {', '.join([str(i) for i in nectar])}")


bees_input = deque(int(i) for i in input().split())
nectar_input = [int(i) for i in input().split()]
symbols_input = deque(i for i in input().split())

honey(bees_input, nectar_input, symbols_input)
