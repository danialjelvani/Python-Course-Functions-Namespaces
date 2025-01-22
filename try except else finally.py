x = 5

try:
    print(x)
    x += 1
except:
    print('cannot print it')
else:
    print('i tried and it worked !')
    print(x)
finally:
    print('i did it all nonetheless')
