import random

def createfile():
    for i in range(10):
        f = open('F:\sendmsg\%s.txt'%i,'a')
        f.write("")
        f.close()

names = []
for i in range(10):
    names.append(i)
    
fileName = 'F:\sndmsg\%s.txt' %random.choice(names)
print(fileName)

