# Given an integer n, count the number of 1's in the binary representation of every number in the range [0, n].
# Return an array output where output[i] is the number of 1's in the binary representation of i.
# Runtime - O(n) assuming n integrs of 32 bits 
class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            count = 0 
            while i > 0:
                if i & 1 == 1:
                    count += 1 
                i = i >> 1
            result.append(count)

        return result 
