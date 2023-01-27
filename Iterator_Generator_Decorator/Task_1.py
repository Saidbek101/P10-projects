def get_next_mutiple(n):
    while True:
        yield n
        n += 2


result = get_next_mutiple(2)

for i in range(4):
    print(next(result))


def get_next_mutiple(n):
    while True:
        yield n
        n += 13


result = get_next_mutiple(13)

for i in range(4):
    print(next(result))

