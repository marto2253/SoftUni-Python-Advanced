
def softuni_party(iters):

    vip = set()
    regular = set()

    for _ in range(iters):
        invitations = input()

        if invitations[0].isdigit():
            vip.add(invitations)
        else:
            regular.add(invitations)

    command = input()
    while command != 'END':
        if command in vip:
            vip.remove(command)
        else:
            regular.remove(command)
        command = input()

    print(len(vip) + len(regular))
    [print(i) for i in sorted(vip)]
    [print(i) for i in sorted(regular)]


iterations = int(input())
softuni_party(iterations)