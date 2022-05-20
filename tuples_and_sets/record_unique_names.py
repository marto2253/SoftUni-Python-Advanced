

def record_unique(iters):

    unique_names = set()

    for _ in range(iters):

        unique_names.add(input())

    [print(i) for i in unique_names]


iterations = int(input())
record_unique(iterations)