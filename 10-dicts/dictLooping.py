from typing import Dict, List # this adds type hints for List and Dict

def get_dict_keys(age_dict: Dict[str, int]) -> List[str]:
    result = []
    for key in age_dict:
        result.append(key)
    return result

def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    result = []
    for key, val in age_dict.items():
        result.append(val)
    return result

# do not modify below this line
dict_1 = {"John": 25, "Doe": 30, "Jane": 22}
dict_2 = {"NeetCode": 24, "NeetCode2": 25, "NeetCode3": 26}

print(get_dict_keys(dict_1))
print(get_dict_keys(dict_2))

print(get_dict_values(dict_1))
print(get_dict_values(dict_2))
