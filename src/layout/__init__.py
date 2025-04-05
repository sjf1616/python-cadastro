def readInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mError: Please, writer a valid number. "Integer"\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[31mError: User dont want to continue or insert data\033[m')
            return 0
        else:
            return n

def collors(color):
    text_color = {
        'clean' : '\033[m',
        'yellow':'\033[33m',
        'white' : '\033[30m',
        'blue':'\033[34m',
        'red':'\033[31m',
        'green':'\033[32m'
    }
    if color in text_color:
        return text_color[color]

def line(weight=30):
    return '-' * weight

def title(txt):
    print(line())
    print(f'{txt:^30}')
    print(line())

def menu(lista):
    title('MENU PRINCIPAL')
    c = 1
    for i in lista:
        print(f'{collors('yellow')}{c}{collors('clean')} - {collors('blue')}{i}{collors('clean')}')
        c += 1
    print(line())

    option = readInt(f'{collors('green')}Sua opção:{collors('clean')}')
    return option