def check_simple(num):
    last_numbers = range(1, num+1)
    for i in last_numbers:
        if num % i == 0 and i != 1 and i != num:
            return False

    return True


def simple_numbers_gen():
    num = 1
    while True:
        if check_simple(num):
            yield num
            num += 1
        else:
            num += 1


gen = simple_numbers_gen()
for _ in range(1000):
    print(next(gen))
