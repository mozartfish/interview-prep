class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        m = -1
        count = 0

        for num in nums:
            if count == 0:
                m = num
                count = 1
            elif m == num:
                count += 1
            else:
                count -= 1

        return m
