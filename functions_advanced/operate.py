def operate(operator, *args):

    def add(*args):
        return sum(args)

    def subtract(x, *args):
        return x + sum(-y for y in args)

    def multiply(*args):
        result = 1
        for number in args:
            result *= number
        return result

    def divide(x, *args):
        result = x
        for number in args:
            result /= number
        return result

    if operator == '+':
        return add(*args)
    elif operator == '-':
        return subtract(*args)
    elif operator == '/':
        return divide(*args)
    elif operator == '*':
        return multiply(*args)

print(operate("+", 1, 2, 3))
print(operate("-", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("/", 3, 4, 2, 3))