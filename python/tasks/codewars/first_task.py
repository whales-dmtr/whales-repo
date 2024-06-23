# Принимает строку, возращает строку со всеми запикаными символами кроме последних четырех.
def maskify(cc):
    seen_part = cc[-4:]
    unknown_part = []
    for i in range(len(cc[:-4])):
        unknown_part.append('#')

    return ''.join(unknown_part) + seen_part

print(maskify(input('---')))