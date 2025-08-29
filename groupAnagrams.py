from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for string in strs:
            key = self.makeKey(string)
            if key not in anagrams:
                anagrams[key].append(string)
            else:
                anagrams[key].append(string)

        return list(anagrams.values())

    def makeKey(self, string):
        chars = [0 for i in range(26)]
        for ch in string:
            chars[ord(ch) - ord("a")] += 1
        return tuple(chars)
