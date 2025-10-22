class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        output =[]
        min_len = min(len(word1),len(word2))
        
        for i in range(min_len):
            output.append(word1[i])
            output.append(word2[i])
        
        output.append(word1[min_len:])
        output.append(word2[min_len:])

        return ''.join(output)