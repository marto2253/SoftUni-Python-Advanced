from collections import deque

fireworks = deque(int(i) for i in input().split(', '))
explosive_powder = [int(i) for i in input().split(', ')]

effects = {
    'Palm Fireworks': 0,
    'Willow Fireworks': 0,
    'Crossette Fireworks': 0,
}

is_prepared = False

while True:

    if effects['Palm Fireworks'] >= 3 and effects['Willow Fireworks'] >= 3 and effects['Crossette Fireworks'] >= 3:
        is_prepared = True
        break
    elif not fireworks or not explosive_powder:
        break

    firework = fireworks.popleft()
    powder = explosive_powder.pop()

    if firework <= 0:
        explosive_powder.append(powder)
        continue
    elif powder <= 0:
        fireworks.appendleft(firework)
        continue

    sum_of_items = firework + powder

    if sum_of_items % 5 == 0 and sum_of_items % 3 == 0:
        effects['Crossette Fireworks'] += 1
    elif sum_of_items % 5 == 0:
        effects['Willow Fireworks'] += 1
    elif sum_of_items % 3 == 0:
        effects['Palm Fireworks'] += 1
    else:
        firework -= 1
        fireworks.append(firework)
        explosive_powder.append(powder)


if is_prepared:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if fireworks:
    print(f"Firework Effects left: {', '.join(str(i) for i in fireworks)}")

if explosive_powder:
    print(f"Explosive Power left: {', '.join(str(i) for i in explosive_powder)}")

for k, v in effects.items():
    print(f'{k}: {v}')
