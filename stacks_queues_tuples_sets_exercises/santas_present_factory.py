from collections import deque


def santas_presents(materials, magic):

    presents = {
        'Bicycle': 0,
        'Doll': 0,
        'Wooden Train': 0,
        'Teddy bear': 0
    }

    while materials and magic:
        last_material = materials.pop()
        first_magic = magic.popleft()

        if last_material == 0 and first_magic == 0:
            continue
        elif last_material == 0:
            magic.appendleft(first_magic)
            continue
        elif first_magic == 0:
            materials.append(last_material)
            continue

        sum = last_material * first_magic

        if sum == 400:
            presents['Bicycle'] += 1
        elif sum == 300:
            presents['Teddy bear'] += 1
        elif sum == 250:
            presents['Wooden Train'] += 1
        elif sum == 150:
            presents['Doll'] += 1
        elif sum < 0:
            materials.append(last_material + first_magic)
        else:
            materials.append(last_material + 15)

    if (presents['Doll'] > 0 and presents['Wooden Train'] > 0) or (presents['Bicycle'] > 0 and presents['Teddy bear'] > 0):
        print("The presents are crafted! Merry Christmas!")
    else:
        print("No presents this Christmas!")

    if materials:
        print(f"Materials left: {', '.join(str(i) for i in reversed(materials))}")
    if magic:
        print(f"Magic left: {', '.join(str(i) for i in magic)}")

    for present, count in sorted(presents.items()):
        if count != 0:
            print(f'{present}: {count}')


materials_for_toys = [int(i) for i in input().split()]
magic_level = deque(int(i) for i in input().split())

santas_presents(materials_for_toys, magic_level)
