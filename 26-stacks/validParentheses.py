class Solution:
    def isValid(self, s: str) -> bool:
        pMap = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            if c in pMap:
                if stack and stack[-1] == pMap[c]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(c)
        return not stack 
