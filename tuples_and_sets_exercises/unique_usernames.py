

def unique_usernames(iters):

    unique_names = set()

    for _ in range(iters):
        unique_names.add(input())

    return [print(i) for i in unique_names]


iterations = int(input())
unique_usernames(iterations)
