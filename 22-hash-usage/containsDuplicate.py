# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
# Runtime - O(n)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        for num in nums:
            if num in numSet:
                return True 
            numSet.add(num)
        return False 