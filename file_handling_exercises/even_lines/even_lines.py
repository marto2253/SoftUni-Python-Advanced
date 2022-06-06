file = open('text.txt', 'r')

special_char = '-,!?.'
counter = 0
for line in file:
    if counter % 2 == 0:
        for char in special_char:
            if char in line:
                while char in line:
                    line = line.replace(char, '@')
        reverse = [i for i in line.split()[::-1]]
        print(' '.join(reverse))
    counter += 1



