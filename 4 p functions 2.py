# make sentence:

import itertools
subs = ['i', 'you']
vers = ['play', 'love']
objs = ['hockey', 'football']


def make_sentence(subjects, verbs, objects):
    sent_list = []
    for s in subjects:
        for v in verbs:
            for o in objects:
                sent = f'{s} {v} {o}'
                sent_list.append(sent)
    return sent_list


print(make_sentence(subs, vers, objs))
print()

# or:

# import itertools baraye sakhte tamame jaygashta:

iter_list = list(itertools.product(subs, vers, objs))

print(iter_list, end='\n\n')

make_sentence2 = []
for x in iter_list:
    a = ' '.join(x)
    make_sentence2.append(a)
print(make_sentence2, end='\n\n')

# or kholase tar baraye emal ru kole list bedune for:

iter_list2 = list(map(lambda x:' '.join(x), iter_list))
print(iter_list2)
