from collections import deque

materials = [int(i) for i in input().split()]
genie_magic = deque(int(i) for i in input().split())

gifts = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0,
}


while materials and genie_magic:
    material = materials.pop()
    magic = genie_magic.popleft()

    total = material + magic

    if total < 100:
        if total % 2 == 0:
            total += material + (magic * 2)
        else:
            total += material + magic
    elif total > 499:
        total /= 2

    if 100 <= total < 200:
        gifts['Gemstone'] += 1
    elif 200 <= total < 300:
        gifts['Porcelain Sculpture'] += 1
    elif 300 <= total < 400:
        gifts['Gold'] += 1
    elif 400 <= total < 500:
        gifts['Diamond Jewellery'] += 1


if gifts['Gemstone'] >= 1 and gifts['Porcelain Sculpture'] >= 1 or gifts['Gold'] >= 1 and gifts['Diamond Jewellery'] >= 1:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f'Materials left: {", ".join(str(i) for i in materials)}')
if genie_magic:
    print(f'Magic left: {", ".join(str(i) for i in genie_magic)}')

gifts_sorted = sorted(gifts.items())
# print(gifts_sorted)
for k, v in gifts_sorted:
    if v != 0:
        print(f'{k}: {v}')
        