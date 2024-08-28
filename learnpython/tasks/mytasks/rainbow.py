import colorama 
import random 

colors = [ 
    colorama.Fore.GREEN,
    colorama.Fore.RED,
    colorama.Fore.YELLOW,
    colorama.Fore.BLUE,
    colorama.Fore.MAGENTA,
    colorama.Fore.CYAN,
]

while True:
    try:
        message = input()
        result = ""
        for letter in message:
            color = colors[random.randint(0, len(colors)-1)]
            result += color + letter

        print(result)
    except EOFError:
        break

