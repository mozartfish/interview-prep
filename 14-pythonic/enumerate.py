from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    for i, num in enumerate(nums):
        if num == 7:
            return i 
    return -1


def get_dist_between_sevens(nums: List[int]) -> int:
    curr_index = -1 
    result = []
    for i, num in enumerate(nums):
        if num == 7 and i > curr_index:
            result.append(i)
            curr_index = i
    
    return result[1] - result[0]


# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
