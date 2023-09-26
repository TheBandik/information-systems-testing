def calc(a, c, b):
    match c:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            return a / b

a, c, b = input().split()
print(calc(int(a), c, int(b)))
