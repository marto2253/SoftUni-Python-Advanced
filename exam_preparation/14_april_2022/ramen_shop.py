from collections import deque

bowls_of_ramen = [int(i) for i in input().split(', ')]
customers = deque(int(i) for i in input().split(', '))


while len(bowls_of_ramen) and len(customers):

    bowl = bowls_of_ramen.pop()
    customer = customers.popleft()

    if bowl == customer:
        continue
    elif bowl > customer:
        bowl -= customer
        bowls_of_ramen.append(bowl)
    else:
        customer -= bowl
        customers.appendleft(customer)

if not customers:
    print("Great job! You served all the customers.")
    if len(bowls_of_ramen) != 0:
        print(f"Bowls of ramen left: {', '.join([str(i) for i in bowls_of_ramen])}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join([str(i) for i in customers])}")
