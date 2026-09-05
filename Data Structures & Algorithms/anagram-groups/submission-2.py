class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmapgroupanagrams = {} # this will contain the final key-value pairs of anagram groups
        finallist = [] # this will be what is returned

        for i in strs:
            sortedanagramgroup = "".join(sorted(i)) # sorted anagram group will be the key in hashmapgroupanagrams
            if sortedanagramgroup not in hashmapgroupanagrams:
                hashmapgroupanagrams[sortedanagramgroup] = [i] # create new list as a value for that key
            else:
                hashmapgroupanagrams[sortedanagramgroup].append(i) # else append the item to the value for that key

        for key, value in hashmapgroupanagrams.items(): # we still need to return the list of lists, so this iterates over the hashmap to do that
            finallist.append(value) 

        return finallist