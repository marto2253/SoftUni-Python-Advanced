
def words_sorting(*args):

    dict = {}

    for word in args:
        sum_of_word = 0
        for letter in word:
            sum_of_word += ord(letter)
        if word not in dict:
            dict[word] = sum_of_word

    result = []
    if sum(dict.values()) % 2 == 0:
        sorted_by_keys = sorted(dict.items(), key= lambda x: x[0])
        for k, v in sorted_by_keys:
            result.append(f'{k} - {v}')
        return '\n'.join(result)

    else:
        sorted_by_values = sorted(dict.items(), key=lambda x: -x[1])
        for k, v in sorted_by_values:
            result.append(f'{k} - {v}')
        return '\n'.join(result)


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print('------------------------------')

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

print('------------------------------')

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))

