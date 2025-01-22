# find the longest and shortest word:

def shortest_longest(sentence: str):
    """
    find the longest and shortest word
    :param:sentence string
    :return: longest and shortest word
    """
    split_list = sentence.split()
    dic1 = {}
    for word in split_list:
        dic1.update({word: len(word)})
    length_list = []
    for k, v in dic1.items():
        length_list.append(v)
    length_list.sort()
    shortest_length = length_list[0]
    longest_length = length_list[-1]
    for k, v in dic1.items():
        if v == shortest_length:
            print(f'"{k}" is the shortest word')
        if v == longest_length:
            print(f'"{k}" is the longest word')


shortest_longest('ali is my best friend from highschool')


# ye k rahe O1 vase peida krdne key az value tu dic:
# dict = { 'ali' : 100 }
# keys = list(dict.keys())
# values = list(dict.values())
# position = values.index(100)
# final_key = keys[position]
# final key = 'ali'
print()

# or:


def shortest_longest2(sentence):
    split_list2 = sentence.split()
    shortest_word = split_list2[0]
    longest_word = split_list2[0]
    for word in split_list2:
        if len(word) <= len(shortest_word):
            shortest_word = word
        if len(word) >= len(longest_word):
            longest_word = word
    print(f'"{shortest_word}" is the shortest')
    print(f'"{longest_word}" is the longest')


shortest_longest2('ali is my best friend from highschool')

print()
# or:
# rahe khafan tar ba moghayese bar asase meyare khodemun:


def shortest_longest3(sentence):
    split_list3 = sentence.split()
    shortest_word = min(split_list3, key=lambda x: len(x))
    longest_word = max(split_list3, key=lambda x: len(x))
    print(f'"{shortest_word}" is the shortest and "{
          longest_word}" is the longest word')


shortest_longest3('ali is my best friend from highschool')
