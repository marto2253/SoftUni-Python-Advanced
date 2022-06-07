import string

file = open('text.txt', 'r')
punctuation = string.punctuation
letters = string.ascii_letters

punctuation_count = 0
letters_count = 0
line_number = 1
for line in file:
    for letter in line:
        if letter in letters:
            letters_count += 1
        elif letter in punctuation:
            punctuation_count += 1

    print(f'Line {line_number}: {line.strip()} ({letters_count})({punctuation_count})')
    line_number += 1
    punctuation_count = 0
    letters_count = 0