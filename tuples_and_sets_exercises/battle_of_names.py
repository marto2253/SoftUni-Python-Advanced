
def battle_of_names(iters):

    odd_numbers = set()
    even_numbers = set()

    for row in range(1, iters+1):
        name = input()

        sum_of_values = 0
        for letter in name:
            ascii_value = ord(letter)
            sum_of_values += ascii_value

        division = int(sum_of_values / row)

        if division % 2 == 0:
            even_numbers.add(division)
        else:
            odd_numbers.add(division)

    if sum(odd_numbers) == sum(even_numbers):
        print(f'{sum(odd_numbers)}, {sum(even_numbers)}')
    elif sum(odd_numbers) > sum(even_numbers):
        print(f'{", ".join([str(i) for i in odd_numbers.difference(even_numbers)])}')
    else:
        print(f'{", ".join([str(i) for i in odd_numbers.symmetric_difference(even_numbers)])}')


iterations = int(input())
battle_of_names(iterations)