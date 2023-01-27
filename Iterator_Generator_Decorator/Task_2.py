def get_next_prime():
    for i in range(2, 1000):
        for j in range(2, i):
            if i % j == 0:
                break

        else:
            yield i


count = get_next_prime()

for _ in range(10):
    print(next(count))
