import pathlib   #pathlib = path location library

s=pathlib.Path('d://LIC.txt')


if (s.exists()):
    print('file already exists')

else:
    f= open('d://LIC.txt','w')
    f.write('my name is zuber')

