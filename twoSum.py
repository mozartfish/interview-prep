class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        index_map = {}
        for indx, val in enumerate(nums):
            diff = target - val
            if diff in index_map:
                return [index_map[diff], indx]
            else:
                index_map[val] = indx

        return [-1, -1]
