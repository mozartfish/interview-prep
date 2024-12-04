class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0
        for n in nums:
            currSum = max(currSum + n, 0)
            maxSum = max(maxSum, currSum)
        return maxSum
        