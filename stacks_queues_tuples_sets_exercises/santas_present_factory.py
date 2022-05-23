from collections import deque

def santas_presents(materials, magic):

    presents = {
        'Bicycle': 0,
        'Doll': 0,
        'Wooden Train': 0,
        'Teddy bear': 0
    }

    while materials and magic:
        last_material = materials[-1]
        first_magic = magic[0]

        if last_material == 0:
            materials.pop()
            continue
        if first_magic == 0:
            magic.popleft()
            continue

        sum = last_material * first_magic

        if sum == 400:
            presents['Bicycle'] += 1
            magic.popleft()
            materials.pop()
        elif sum == 300:
            presents['Teddy bear'] += 1
            magic.popleft()
            materials.pop()
        elif sum == 250:
            presents['Wooden Train'] += 1
            magic.popleft()
            materials.pop()
        elif sum == 150:
            presents['Doll'] += 1
            magic.popleft()
            materials.pop()
        elif sum < 0:
            magic.popleft()
            materials.pop()
            materials.append(abs(last_material + first_magic))
        else:
            magic.popleft()
            materials[-1] += 15

    if presents['Doll'] >= 1 and presents['Wooden Train'] >= 1 or presents['Bicycle'] >= 1 and presents['Teddy bear'] >= 1:
        print("The presents are crafted! Merry Christmas!")
    else:
        print("No presents this Christmas!")

    if len(materials) != 0:
        print(f"Materials left: {', '.join(str(i) for i in materials)}")
    if len(magic) != 0:
        print(f"Magic left: {', '.join(str(i) for i in magic)}")

    for present, count in sorted(presents.items()):
        if count != 0:
            print(f'{present}: {count}')


materials_for_toys = [int(i) for i in input().split()]
magic_level = deque(int(i) for i in input().split())

santas_presents(materials_for_toys, magic_level)
