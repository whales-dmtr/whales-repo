from math import prod


def factorials():
    num = 1
    while True:
        yield prod(range(1, num+1))
        num += 1


gen = factorials()
for _ in range(10):
    print(next(gen))
