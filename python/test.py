import re

with open(file='docs/basic_python.txt', mode='r', encoding='UTF-8') as f:
    file_string = f.read()
    result = re.search(file_string, 'выражения')
    print(result)
