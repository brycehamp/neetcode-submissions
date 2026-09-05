class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmapgroupanagrams = {} # this will contain the final key-value pairs of anagram groups

        for i in strs:
            sortedanagramgroup = "".join(sorted(i)) # sorted anagram group will be the key in hashmapgroupanagrams
            if sortedanagramgroup not in hashmapgroupanagrams:
                hashmapgroupanagrams[sortedanagramgroup] = [i] # create new list as a value for that key
            else:
                hashmapgroupanagrams[sortedanagramgroup].append(i) # else append the item to the value for that key

        return list(hashmapgroupanagrams.values())