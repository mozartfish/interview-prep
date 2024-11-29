def get_longer_word(word1: str, word2: str) -> str:
    w1_len = len(word1)
    w2_len = len(word2)
    if w1_len >= w2_len:
        return word1
    else:
        return word2



# do not modify below this line
print(get_longer_word("yellow", "orange"))
print(get_longer_word("red", "blue"))
print(get_longer_word("green", "blue"))
