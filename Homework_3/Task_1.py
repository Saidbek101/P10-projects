def odd_number():
    try:
        for num in range(1, 21):
            if num % 2 == 0:
                print(num * -1)
            else:
                yield num
    except StopIteration:
        print("Error")

    return odd_number


generator = iter(odd_number())

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

