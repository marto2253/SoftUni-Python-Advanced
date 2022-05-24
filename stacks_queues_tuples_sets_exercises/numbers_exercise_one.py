
def numbers(seq_one, seq_two):

    iterations = int(input())

    for _ in range(iterations):

        command = input().split()

        if command[0] == 'Add':
            if command[1] == 'First':
                for i in command:
                    if i.isdigit():
                        seq_one.add(int(i))
            else:
                for i in command:
                    if i.isdigit():
                        seq_two.add(int(i))
        elif command[0] == 'Remove':
            if command[1] == 'First':
                for i in command:
                    if i.isdigit() and int(i) in seq_one:
                        seq_one.remove(int(i))
            else:
                for i in command:
                    if i.isdigit() and int(i) in seq_two:
                        seq_two.remove(int(i))
        else:
            if seq_one.issubset(seq_two) or seq_two.issubset(seq_one):
                print('True')
            else:
                print('False')

    print(", ".join(str(i) for i in sorted(seq_one)))
    print(", ".join(str(i) for i in sorted(seq_two)))


sequence_one = set([int(i) for i in input().split(' ')])
sequence_two = set([int(i) for i in input().split(' ')])

numbers(sequence_one, sequence_two)

