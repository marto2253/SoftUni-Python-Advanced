from collections import deque

elves_energy = deque(int(i) for i in input().split())
num_of_materials = [int(i) for i in input().split()]

# print(elves_energy)
# print(num_of_materials)

counter = 0
toys_created = 0
energy_spent = 0

while True:

    current_elf = elves_energy.popleft()
    current_material = num_of_materials.pop()
    counter += 1

    if current_elf < 5:
        if len(elves_energy) <= 0:
            break
        num_of_materials.append(current_material)
        continue

    if current_material > current_elf:
        num_of_materials.append(current_material)
        elves_energy.append(current_elf * 2)
        continue

    if current_material * 2 > current_elf and counter % 3 == 0:
        num_of_materials.append(current_material)
        elves_energy.append(current_elf * 2)
        continue

    if counter % 3 == 0 and (current_material * 2) <= current_elf:
        if counter % 5 != 0:
            toys_created += 2
        energy_spent += current_material * 2
        current_elf -= (current_material * 2)
        current_elf += 1
        elves_energy.append(current_elf)
        continue
    elif counter % 5 == 0 and current_material <= current_elf:
        current_elf -= current_material
        energy_spent += current_material
        continue
    else:
    # if current_material <= current_elf and counter % 3 != 0 and counter % 5 != 0:
        toys_created += 1
        energy_spent += current_material
        current_elf -= current_material
        current_elf += 1
        elves_energy.append(current_elf)

    if len(elves_energy) == 0 or len(num_of_materials) == 0:
        break

print(f'Toys: {toys_created}')
print(f'Energy: {energy_spent}')

if not num_of_materials:
    print(f'Elves left: {", ".join([str(i) for i in elves_energy])}')
else:
    print(f'Boxes left: {", ".join([str(i) for i in num_of_materials])}')