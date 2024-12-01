# Given a 32-bit unsigned integer n, reverse the bits of the binary representation of n and return the result.
# Runtime - O(1) assuming constant of 32 bit integers 

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0 
        for i in range(32):
            bit = (n >> i) & 1
            result = result | (bit << (31 - i))
        return result 
        