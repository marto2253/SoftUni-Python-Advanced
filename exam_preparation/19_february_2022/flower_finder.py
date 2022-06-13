from collections import deque

vowels = deque(i for i in input().split())
consonaunts = [i for i in input().split()]

words = ['rose', 'tulip', 'lotus', 'daffodil']
current_letters = set()
word_found = False

while vowels and consonaunts:
    vowel = vowels.popleft()
    consonaunt = consonaunts.pop()

    current_letters.add(vowel)
    current_letters.add(consonaunt)

    for word in words:
        counter = 0
        for letter in current_letters:
            if letter in word:
                counter += word.count(letter)
        if len(word) == counter:
            print(f'Word found: {word}')
            word_found = True
            break

    if word_found:
        break

if not word_found:
    print('Cannot find any word!')
if vowels:
    print(f'Vowels left: {" ".join(vowels)}')
if consonaunts:
    print(f'Consonants left: {" ".join(consonaunts)}')


