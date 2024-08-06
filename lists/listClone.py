from typing import List
import copy 

def remove_element(arr: List[int], element: int) -> List[int]:
    # shallow copy 
    cloned_list = arr.copy()
    cloned_list.remove(element)

    # deep copy 
    deep_list = copy.deepcopy(arr)
    # return deep_list
    
    return cloned_list



# do not modify below this line
arr = [1, 3, 5, 7, 9]

print(remove_element(arr, 3))
print(arr)
print(remove_element(arr, 9))
print(arr)
print(remove_element(arr, 1))
print(arr)
