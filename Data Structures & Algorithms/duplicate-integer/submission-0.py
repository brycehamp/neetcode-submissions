class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashsetnums = set()
        for n in nums:
            if hashsetnums and n in hashsetnums:
                return True
            else:
                hashsetnums.add(n)
        return False