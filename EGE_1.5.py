# EGE 1.5

def convert_to(a, x):
    assert isinstance(a, int), 'Ошибка типа данных, переменная "a"!'
    assert isinstance(x, int), 'Ошибка типа данных, переменная "x"!'
    s = ''
    while a > 0:
        s += str(a % x)
        a //= x
    return s

a = int(input())
b = convert_to(a, 4)

if a % 4 == 0:
    b += b[-2:]
else:
    b += convert_to(a % 4 * 2, 4)

b = int(b, 4)
print(b)