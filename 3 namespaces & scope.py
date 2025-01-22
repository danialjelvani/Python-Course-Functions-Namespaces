# hatta tu del ham az LEGB peiravi mikone
# local enclosing global built-in
# locals() va globals() ro agar print bgirim neshunemun mide
# globals() o locals() ye functionan k returneshun dictionarye vase
# hamin badesh [] ro mizarim vase khundne key o value

x = 2
print(globals()['x'])

# mishe taghir tu globals dad ama tu locals na:

globals()['x'] = 'danial'
print(x)

print('d' in globals()['x'])

# global declaration:
# vase ine k agar tu local taghiri tu var ijad krdim
# tu global ham emal she:

y = 3


def f1():
    global y
    y = 8
    print(y)


f1()
print(y)

# nonlocal vase localo enclosing declaratione:


def f2():
    z = 1

    def f3():
        nonlocal z
        z = 2
    f3()
    print(z)


f2()
