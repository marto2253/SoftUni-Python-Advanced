
def stundets_grades(num_of_iters):

    grades = {}

    for _ in range(num_of_iters):
        name, grade = input().split()

        if name not in grades:
            grades[name] = list()

        grades[name].append(float(grade))

    # print(grades)

    for k, v in grades.items():
        formatted_grades = " ".join([f'{i:.2f}' for i in v])
        print(f'{k} -> {formatted_grades} (avg: {sum(v) / len(v):.2f})')


num_of_iters = int(input())
stundets_grades(num_of_iters)
