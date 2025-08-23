class Solution:
    def lengthOfLastWord(self, s: str) -> int: 
        length = 0
        i = 1
        c = s[len(s)-i]
        while length == 0:
            if c != ' ':
                length+=1
            i+=1
            c = s[len(s)-i] 
        
        while i <= len(s) and c != ' ':
            length+=1
            i+=1
            c = s[len(s)-i] 
        return length
