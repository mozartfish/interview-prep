# Given an integer array arr, return the length of a maximum size turbulent subarray of arr.
# A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.
# More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:
#     For i <= k < j:
#         arr[k] > arr[k + 1] when k is odd, and
#         arr[k] < arr[k + 1] when k is even.
#     Or, for i <= k < j:
#         arr[k] > arr[k + 1] when k is even, and
#         arr[k] < arr[k + 1] when k is odd.
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        L, R = 0, 1 
        res, prev = 1, ""
        while R < len(arr):
            if arr[R - 1] > arr[R] and prev != ">":
                res = max(res, R - L + 1)
                R += 1
                prev = ">"
            elif arr[R - 1] < arr[R] and prev != "<":
                res = max(res, R - L + 1)
                R += 1 
                prev = "<"
            else:
                if arr[R] == arr[R - 1]:
                    R += 1
                L = R - 1
                prev = ""
        return res 