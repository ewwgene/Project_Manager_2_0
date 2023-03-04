from time import sleep
from random import randrange, choice
from sys import stderr, stdout

def main():
    options = 2 * ['good'] + ['bad']
    with open('log.txt', 'w') as f:
        for i in range(10):
            sleep(randrange(1, 3))
            option = choice(options)
            if option == 'good':
                ###############
                #stdout.write('good')
                #stdout.flush()
                ###############
                pf('good', end='')
            else:
                ###############
                #stderr.write('bad')
                #stderr.flush()
                ###############
                pf('bad', end='')
                sleep(1)
                pf('end of speak', end='')
                ###############
                #f.write(option + '\n')
                #f.flush()
                ###############

def pf(string, **kwargs): #if you want to use print('',flush = True) instead of stdout or stderr
    if 'flush' in kwargs:
        print(string, **kwargs)
    else:
        print(string, flush = True, **kwargs)

if __name__ == '__main__':
    main()