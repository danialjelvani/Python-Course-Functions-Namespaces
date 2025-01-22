# string.join(iterable) miad beine iterable ha string ro mizare:

a = '--'.join(['danial', 'mahsa'])
print(a)

# harchi bade *args biad mishe
# keyword only argument chon harchi
# ghable keyword bashero mikeshe tu khodesh:


def pre(*args, prefix='salam'):
    print(f'{prefix} {args}')


pre('ali', 'hasan', 'hosein')
pre('ali', 'hasan', 'hosein', prefix='hi')


# age khasim hatman type kone keywordo bayad az
# ignore estefade knim

def oper(x, y, *ignore, op=''):
    if op == '+':
        print(x+y)
    if op == '-':
        print(x-y)


oper(3, 5, 5, 45, 46, 221, op='+')

# age * bezarim khate payane positional argumenta
# miduneo badish mishe keyword


def oper2(x, y, *, op=''):
    if op == '+':
        print(x+y)
    if op == '-':
        print(x-y)


oper2(6, 9, op='+')

# positional only argument ba / hast
# va edamash mishe tarkibe positionalo keyword k age
# badesh * biad unvagh bade setare mishe faht keyword
# mesale positional only len(x) hast


def oper3(x, /, y, *, op=''):
    if op == '+':
        print(x+y)
    if op == '-':
        print(x-y)


oper2(6, y=3, op='+')

# in halate * avale function shaye e k eshteba kam she:


def oper4(*, num1: float, num2: float, op: str = '') -> float:
    '''
    operate plus & minus

    :param num1: first input
    :param num2: second input

    :return: plus & minus

    '''
    if op == '+':
        print(num1+num2)
    if op == '-':
        print(num1-num2)


oper4(num2=2, num1=7, op='-')


# docstring mese balast
# funtion annotation yani note mizari k har arg ya keyword az che jensi
# bashe masalan int ya float ya list vali error nmide serfn etela resani mikone
# mypy force mikone va mese from typing import list ...
