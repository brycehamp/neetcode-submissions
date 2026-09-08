class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmapnumsoccurrences = defaultdict(int)
        hashmapnumsoccurrences.update(dict.fromkeys(nums,0)) # hashmapnumsoccurrences now contains nums as keys and 0 as the value for each key
        buckets = defaultdict(list)
        highestkkeys = []

        for entry in nums:
            hashmapnumsoccurrences[entry] += 1 

        # hashmapnumsoccurrences now has keys and the number of times they occur
        
        for entry, count in hashmapnumsoccurrences.items():
            buckets[count].append(entry)

        # buckets now contains what is essentially a reversal of hashmapnumsoccurrences, where the number of occurences is the key and the unique entries in nums are the values. this allows us to record the highest occurring values in highestkkeys:

        for i in range(len(nums), 0, -1):
            for entry in buckets[i]:
                highestkkeys.append(entry)
                if len(highestkkeys) == k:
                    return highestkkeys
                  
        return highestkkeys