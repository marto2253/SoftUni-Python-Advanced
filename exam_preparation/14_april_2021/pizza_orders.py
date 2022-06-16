from collections import deque

orders = deque(int(i) for i in input().split(', '))
employees = [int(i) for i in input().split(', ')]

total_pizzas = 0

while orders and employees:
    order = orders.popleft()
    employee = employees.pop()

    if 0 >= order or order > 10:
        employees.append(employee)
        continue

    if order <= employee:
        total_pizzas += order
    else:
        order -= employee
        total_pizzas += employee
        orders.appendleft(order)

if not orders:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {total_pizzas}')
    print(f'Employees: {", ".join(str(i) for i in employees)}')
else:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join(str(i) for i in orders)}')

