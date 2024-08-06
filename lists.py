# resizable lists part 1
my_list = [1, 2, 3]
# append
# [1, 2, 3, 4]
my_list.append(4) 
# [1, 2, 3, 4, 5]
my_list.append(5) 

# pop
# [1, 2, 3, 4]
my_list.pop() 

# insert
# [1, 3, 2, 3, 4]
my_list.insert(1, 3) 

# resizable lists part 2 
my_list = [1, 3, 2, 3]

# index
# 1
my_list.index(3) 

# remove
# [1, 2, 3]
my_list.remove(3) 

# extend
# [1, 2, 3, 4, 5]
my_list.extend([4, 5]) 

# in 
my_list = [1, 2, 3]
if 3 in my_list:
    print("3 is in the list")

# concat 
list1 = [1, 2, 3]
list2 = [4, 5, 6]
# [1, 2, 3, 4, 5, 6]
result = list1 + list2 

# list initialization 
my_list = [0] * 5
my_list = [1] * 3

# list clone 
# shallow copy 
# copy 
original_list = [1, 2, 3]
cloned_list = original_list.copy()
# slice 
original_list = [1, 2, 3]
cloned_list = original_list[:]
# list constructor
original_list = [1, 2, 3]
cloned_list = list(original_list)

# deep copy 
import copy
original_list = [[1, 2], [3, 4]]
cloned_list = copy.deepcopy(original_list)

# list comprehension 
# original 
my_list = [i for i in range(5)]
# [0, 1, 2, 3, 4]
print(my_list) 

# zip comprehension 
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
result = [i + j for i, j in zip(arr1, arr2)]

# condition comprehension 
arr = [1, 2, 3, 4, 5]
result = [i for i in arr if i % 2 == 0]




