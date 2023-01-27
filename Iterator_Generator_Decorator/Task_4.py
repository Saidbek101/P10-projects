def only_even_parameters(fun):
    def plus_inner(*args):

        for arg in args:
            if arg % 2 != 0:
                return 'Please add only even numbers!'

        return fun(*args)

    return plus_inner


@only_even_parameters
def add_multiply(a, b, c, d):
    return a * b * c * d


@only_even_parameters
def add_numbers(a, b):
    return a + b


print(add_numbers(6, 8))
print(add_multiply(1, 4, 4, 2))
