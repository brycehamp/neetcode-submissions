class Solution:

    def encode(self, strs: List[str]) -> str:
        strcombined = ""

        for s in strs:
            strcombined += f"{len(s)}#" + s

        return strcombined

    def decode(self, s: str) -> List[str]:
        liststrs = []
        intcurrent_index = 0
        intcounter = 0

        while intcurrent_index < len(s):
            strtemp_length = "" # this will be how we retrieve the number in front of the pound sign
            strtemp_word = "" # the section of s that will comprise the word that will be appended to liststrs

            while s[intcurrent_index] != "#":
                strtemp_length += s[intcurrent_index]
                intcurrent_index += 1

            intcurrent_index += 1 # still need to increment by 1 to start with the first letter of the next word

            intcounter = int(strtemp_length) # intcounter is now the length of the next string within s
            intword_position_in_s = intcurrent_index + intcounter # the ending index of the next string in s

            while intcurrent_index < intword_position_in_s:
                strtemp_word += s[intcurrent_index]
                intcurrent_index += 1

            liststrs.append(strtemp_word)
            
        return liststrs
