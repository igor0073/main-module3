def test(txt, *params, types='это кaртеж, дальше словарь', **valeus):
    print(txt, params, types, valeus)


test('я понял', 1, 2, 3, 4, 5, name='Igor', cours='Python')


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(7))
