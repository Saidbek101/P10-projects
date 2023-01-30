def get_planets():
    with open('task_planets_3.txt', 'r') as file:
        reader = file.readlines()
    return reader


def planets_gen():
    information = get_planets()
    for a in information:
        if 'name' in a:
            yield a.split('=')[1]


result = iter(planets_gen())
print(next(result))
print(next(result))
print(next(result))
print(next(result))

