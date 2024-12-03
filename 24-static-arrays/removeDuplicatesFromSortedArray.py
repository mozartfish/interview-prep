class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        k = 1
        while i < len(nums):
            if nums[i-1] == nums[i]:
                i += 1 
            else:
                nums[k] = nums[i]
                i += 1 
                k += 1 
        return k
        