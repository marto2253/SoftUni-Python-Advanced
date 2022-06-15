
def shopping_list(budget: int(), **kwargs):
    if budget < 100:
        return 'You do not have enough budget.'

    bought_items = {}

    for item, price in kwargs.items():
        price = price[0] * price[1]

        if len(bought_items) == 5:
            break

        if budget >= price:
            bought_items[item] = price
            budget -= price

    result = []

    for k, v in bought_items.items():
        result.append(f'You bought {k} for {v:.2f} leva.')

    return '\n'.join(result)


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

print('-------------------------------')

print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))

print('-------------------------------')

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
