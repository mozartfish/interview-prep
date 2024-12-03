class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        newLen = 2 * n 
        ans = [0] * newLen


        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        return ans
        