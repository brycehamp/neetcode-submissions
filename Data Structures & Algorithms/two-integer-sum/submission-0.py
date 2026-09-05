class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmapnums = {}

        for i, num in enumerate(nums):
            seekingvalue = target - num # seekingvalue is a possible value we want to find

            if seekingvalue in hashmapnums: # if that value is in the hashmap
                return [hashmapnums[seekingvalue], i]
            
            hashmapnums[num] = i # insert each value in nums into a hashmap along with their index

        return None
