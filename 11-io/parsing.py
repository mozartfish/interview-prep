from typing import List

def read_integers() -> List[int]:
    user_input = input()
    nums = user_input.split(",")
    result = []
    for num in nums:
        result.append(int(num))
    return result

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())