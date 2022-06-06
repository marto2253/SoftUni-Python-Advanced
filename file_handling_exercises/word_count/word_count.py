
dd ={}

with open('.\\words.txt', 'r') as words_file:
    words_list = words_file.read().split(' ')

    for word in words_list:
        count = 0
        with open('input.txt', 'r') as input_file:
            input_file_contents = input_file.read().lower().split()
            for content in input_file_contents:
                if content.strip('.?!-,') == word:
                    count += 1

            dd[word] = count

a= sorted(dd.items(), key=lambda x: -x[1])

for w, c in a:
    print(w,'-',c)

