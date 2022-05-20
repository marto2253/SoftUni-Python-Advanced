
def periodic_table(iters):

    unique_elements = set()

    for _ in range(iters):
        elements = input().split()

        for element in elements:
            if element not in unique_elements:
                unique_elements.add(element)

    [print(i) for i in unique_elements]


iterations = int(input())
periodic_table(iterations)
