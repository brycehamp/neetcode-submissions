class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestseq = 0

        setnums = set(nums)

        for n in setnums:
            if n-1 not in setnums:
                templongestseq = 0

                while n in setnums:
                    templongestseq +=1
                    n+=1
            
                longestseq = max(templongestseq, longestseq)
            
        return longestseq