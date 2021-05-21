def add(*args):
    sum = 0
    for number in args:
        sum += number
    print(sum)


add(2, 3, 4, 5, 6)


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]

    return n


print(calculate(2, add=3, multiply=5))


class Car():
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.year = kw.get('year')


car = Car(make='Volkswagen', model='Jetta GLI')

print(car.make)
print(car.model)
print(car.year)
