def stock_availability(*args):

    inventory = args[0]
    status = args[1]
    other = args[2:]

    if status == 'delivery':
        inventory.extend(other)
    elif status == 'sell':
        if not other:
            inventory.pop(0)
        for item in other:
            if type(item) is int:
                inventory = inventory[int(item):]
            else:
                while item in inventory:
                    inventory.remove(item)

    return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
