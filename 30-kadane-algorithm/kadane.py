# find a non-empty subarray with the largest sum

nums = [4, -1, 2, -7, 3, 4]
def bruteForce(nums):
    maxSum = nums[0]
    # i starting pointer 
    # j incrementing pointer 
    for i in range(len(nums)):
        currSum = 0
        for j in range(i, len(nums)):
            # print(f"i: {i}", f"j: {j}")
            # print(f"maxSum: {maxSum}")
            currSum += nums[j]
            # print(f"current sum: {currSum}")
            maxSum = max(maxSum, currSum)
    print(f"maxSum - bruteForce: {maxSum}")
    return maxSum 

def kadane(nums):
    maxSum = nums[0]
    currSum = 0 
    for n in nums:
        # currSum = max(currSum, 0)
        # currSum += n 
        currSum = max(currSum + n, 0)
        maxSum = max(maxSum, currSum)
    print(f"maxSum - kadane: {maxSum}")
    return maxSum

def slidingKadane(nums):
    maxSum = nums[0]
    currSum = 0
    maxL, maxR = 0 
    L = 0 
    for R in range(len(nums)):
        if currSum < 0:
            currSum = 0 
            L = R 
        currSum += nums[R]
        if currSum > maxSum:
            maxSum = currSum
            maxL, maxR = L, R 
    return [maxL, maxR]

bruteForce(nums)
kadane(nums)