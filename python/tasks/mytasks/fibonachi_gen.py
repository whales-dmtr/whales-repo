def gen_fibonacci(max_value):
    last = 0
    current = 1
    while last < max_value:
        yield last
        last, current = current, last + current


for i in gen_fibonacci(100):
    print(i)
