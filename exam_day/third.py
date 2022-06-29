
def shopping_cart(*args):

    meals = {
        'Pizza': [],
        'Soup': [],
        'Dessert': [],
    }

    for item in args:
        if item == 'Stop':
            break
        if item[0] == 'Pizza':
            if item[1] not in meals[item[0]] and len(meals[item[0]]) < 4:
                meals[item[0]].append(item[1])
        elif item[0] == 'Soup':
            if item[1] not in meals[item[0]] and len(meals[item[0]]) < 3:
                meals[item[0]].append(item[1])
        elif item[0] == 'Dessert':
            if item[1] not in meals[item[0]] and len(meals[item[0]]) < 2:
                meals[item[0]].append(item[1])

    result = ''
    sorted_meals = sorted(meals.items(), key= lambda x: (-len(x[1]), x[0]))

    items = [*meals.values()]
    count = 0
    for item in items:
        if len(item) == 0:
            count += 1

    if count == 3:
        return 'No products in the cart!'

    for k, v in sorted_meals:
        sorted_values = sorted(v)
        result += f'{k}:\n'
        for value in sorted_values:
            result += f' - {value}\n'

    return result.strip()

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print('----------------------------------')

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print('----------------------------------')

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
