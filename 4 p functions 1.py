# char count

from collections import Counter


def count_char(a: str):
    dic1 = {}
    for x in a:
        b = a.count(x)
        dic1.update({x: b})
    print(dic1)


count_char('danial')

# or:

# dic.get(key,default value) default value mide b key agar key tu dic nabashe
my_string = 'danial'
dic2 = {}
for x in my_string:
    dic2[x] = dic2.get(x, 0) + 1
print(dic2)

# or:

dic3 = {}
for x in my_string:
    y = 1
    if x in dic3:
        dic3[x] += 1
    else:
        dic3[x] = 1
print(dic3)

# or:

# from collections import Counter

print(Counter(my_string))
