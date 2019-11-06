import random
esc = list('ABCDEFGHIJLMNOPRSTUV')
boo = True
while (boo):
    if (len(esc) == 1):
        print(esc[0])
        boo = False
    else:
        i = random.randint(0, (len(esc) - 1))
        print(esc[i])
        esc = esc[:i] + esc[i+1:]
        teste = input('')
        if (teste != ''):
            boo = False
    
