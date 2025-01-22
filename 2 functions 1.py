# / taghsime // taghsime sahihe

def average(a):
    total = 0
    for x in a:
        total += x
    return total/len(a)


print(average([3, 5]))

# arg unpacking:
# baraye balayi bayad hatmn argument haro tu
# ye listi mizashtim moghe vorudi def grftn vali ba unpack dg niaz nis:


def average2(*a):
    total = 0
    for x in a:
        total += x
    return total/len(a)


print(average2(5, 6, 7, 8))

pack = [2, 3, 4]
print(average2(*pack))

# kwargs miad keyword ham unpack mikone tu dictionary:


def print_age(**kwargs):
    print(kwargs)
    print()
    for k, v in kwargs.items():
        print(f'{k:8} is {v:2} years old')


print_age(ali=3, reza=4, mahsa=9)
print()
dict1 = {
    'danial': 19,
    'alireza': 20,
}
print_age(**dict1)

# * vase tuple e ** vase dictionary ba har esmi

# yeki az rah haye khube merge dictionary ha unpack krdneshunn tu dic jadide:
# ye rah dg ham | e:

dict2 = {
    'mohesn': 17,
    'hashem': 18,
}
print()
dict3 = {**dict1, **dict2}
dict4 = dict1 | dict2
print(dict3, dict4, sep='\n')


def f(*args, **kwargs):
    print(f'args:    {args}')
    print(f'kwargs:  {kwargs}')

# *args tuple misheo **kwargs dictionary:


f(1, 2, 3, ali=5, danial=9)
