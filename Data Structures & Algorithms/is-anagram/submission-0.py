class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmaps = {}
        hashmapt = {}

        for char in s:
            if char not in hashmaps:
                hashmaps[char] = 0
            else:
                hashmaps[char] +=1

        for char in t:
            if char not in hashmapt:
                hashmapt[char] = 0
            else:
                hashmapt[char] +=1

        if (hashmaps == hashmapt):
            return True

        return False