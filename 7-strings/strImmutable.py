def remove_fourth_character(word: str) -> str:
    previous = word[:3]
    next_word = word[4:]
    return previous + next_word


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
