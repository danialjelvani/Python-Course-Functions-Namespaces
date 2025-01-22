def factor(q, f, p):
    print(f'{q} {f}s cost {p} $')

# q,p,f formal parameteran
# 6 , moz, 100 actual parameteran
# ina required positional argumentan
# yani hamishe bayad 3 tashun bashn


print(factor(6, 'moz', 100))

# keyword argument hm darim:
# k ina ham required an

print(factor(f='sib', q=5, p=80))

# default parameter k required nashe:


def factor2(f, q=10, p=30):
    print(f'{q} {f}s cost {p} $')


print(factor2('golabi'))
print(factor2('golabi', 5))
print(factor2('golabi', 5, 70))


def addchar(l1=[]):
    l1.append('*')
    print(l1)


print(addchar())
print(addchar())
print(addchar())

# tebghe bala default value taghir
# mikone mutable bashe
# b hamin khater age khasim ye iterable
# bezarim k taghir nkne shart midim:


def addchar2(l1=None):
    if l1 is None:
        l1 = []
    l1.append('+')
    print(l1)

# tu khode function print has dg
# printe function nmikhad vase hamin
# ghablia None mizad


addchar2()
addchar2()
addchar2()

print('\nfunction 1 :\n')
# return baes mishe betunim taghir bdim iterable ro:
# khorujie asli function ma dar asl return e
# va print serfan ye namayesh zahere
# vase hamin vaghti mizni print(function) none mide
# age return ee nadashte bashim

y = 5


def f(x):
    x = 10
    print(x)


f(y)
print()

print(f(y))
print()

print(y)
print('\nfunction 2 :\n')
# dar bala taghir nadad y ro


def f2(x):
    x = 10
    print(x)
    return x*3


f2(y)
print()

print(f2(y))
print()

print(y)
print()

# agar khasim return chanta khoruji bede
# behtare tu iterable nazarim masalan bezarim tu tuple
# k age hichi nazarim serfan , khodesh mizare tu tuple

z = f2(3)*3
print(z)
# pas khoruji moheme na print
