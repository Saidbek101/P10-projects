def add_numbers(fun):
    def plus_inner(a, b):
        try:
            return fun(a, b)
        except:
            print("Error")

    return plus_inner

@add_numbers
def added(a, b):
    return a * 2 + b * 2


print(added(2, 3))



