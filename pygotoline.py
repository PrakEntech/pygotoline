def gotoline(x):
    import os
    f1 = open(os.path.basename(__file__),mode = 'r')
    data = f1.readlines()
    f1.seek(0)
    for i in range(len(data)):
        if f1.readline()=='#'+x+'\n':
            break
    data = f1.readline()
    f1.close()
    if '#' in data:
        try:
            data = data.replace('#','')
            return eval(data)
        except EOFError:
            pass
    else:
        return eval(data)        
print('HELLO')
#a
#print(WORLD)
print('Calling FUNCTION....')
for i in range(5):
    gotoline('a')

