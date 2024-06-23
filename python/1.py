def generator():
    yield 1
    yield 2
    yield 3


print(list(generator()))  # [1, 2, 3]
