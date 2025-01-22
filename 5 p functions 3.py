
# check if all alphabets r in the sentence:

def is_pangram(sentence: str) -> bool:
    is_valid = True
    for x in 'abcdefghijklmnopqrstuvwxyz':
        if x not in sentence.lower():
            is_valid = False
    return is_valid


print(is_pangram('the quick brown fox jumps over the lazy dog'))
