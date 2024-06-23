from mytasks.time_fn import time_fn


def is_even(numb):  # True - четный
    return numb % 2 == 0


@time_fn
def diamond(n):
    if is_even(n) or n <= 0:
        return None

    str = ''

    current_steps = 1
    step = n // 2
    count_added_asterisk = 2
    count_spaces = (n - current_steps) // 2

    for i in range(step):
        str += (' ' * count_spaces)
        str += ('*' * current_steps)
        str += '\n'
        current_steps += count_added_asterisk
        count_spaces = (n - current_steps) // 2

    str += ('*' * n) + '\n'
    current_steps -= count_added_asterisk
    count_spaces = 1

    for i in range(step):
        str += (' ' * count_spaces)
        str += ('*' * current_steps)
        str += '\n'
        current_steps -= count_added_asterisk
        count_spaces = (n - current_steps) // 2

    return str


number = int(input("Type number: "))

print(diamond(number))
