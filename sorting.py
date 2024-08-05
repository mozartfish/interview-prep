# ascending
elements = [5, 3, 6, 2 ,1]
elements.sort()
# [1, 2, 3, 5, 6]
print(elements)

elements = ["grape", "apple", "banana", "orange"]
elements.sort()
# ["apple", "banana", "grape", "orange"]
print(elements)

# descending 
elements = [5, 3, 6, 2, 1]
# [6, 5, 3, 2, 1]
elements.sort(key=None, reverse=True)
print(elements) 


# custom sort 
# sort by word length 
def get_word_length(word: str) -> int:
    return len(word)

words = ["apple", "banana", "kiwi", "pear", "watermelon", "blueberry", "cherry"]
words.sort(key=get_word_length)
# ['kiwi', 'pear', 'apple', 'banana', 'cherry', 'blueberry', 'watermelon']
print(words)

# lambda function sorts 
words = ["apple", "banana", "kiwi", "pear", "watermelon", "blueberry", "cherry"]
words.sort(key=lambda word: len(word))
# ['kiwi', 'pear', 'apple', 'banana', 'cherry', 'blueberry', 'watermelon']
print(words) 

# sorted 
words = ["kiwi", "pear", "apple", "banana", "cherry", "blueberry"]
sorted_words = sorted(words)
# ['apple', 'banana', 'blueberry', 'cherry', 'kiwi', 'pear']
print(sorted_words) 


