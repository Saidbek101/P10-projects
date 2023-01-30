def get_words():
    result = []
    with open('test_2.txt', 'r') as file:
        reader = file.read()
        for i in reader:
            result.append(i)
    return result


def genera():
    information = get_words()
    for i in information:
        yield i


generator = iter(genera())
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
