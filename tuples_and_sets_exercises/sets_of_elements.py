
def sets_of_ele(iters):
    first_iter = int(iters[0])
    second_iter = int(iters[1])

    first_set = set()
    second_set = set()

    for _ in range(first_iter):
        first_set.add(int(input()))

    for _ in range(second_iter):
        second_set.add(int(input()))

    [print(i) for i in first_set.intersection(second_set)]


iterations = input().split()
sets_of_ele(iterations)
