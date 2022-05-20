
expression = input()

result = {}

for letter in expression:
    if letter not in result:
        result[letter] = 0
    result[letter] += 1

for k, v in sorted(result.items()):
    print(f'{k}: {v} time/s')
