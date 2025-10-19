class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        m1=0
        m2=0
        rstring =""
        flag=True
        while len(rstring) < len(word1)+len(word2):
            print("Reached while + Current:"+rstring)
            if flag:
                if m1 < len(word1):
                    rstring= rstring+(word1[m1])
                    m1 +=1
                else:
                    if m2 < len(word2):
                        rstring= rstring+ (word2[m2:len(word2)])
                        return rstring
                    else:
                        return rstring
                flag = False
            else:
                if m2 < len(word2):
                    rstring=rstring+(word2[m2])
                    m2+=1
                else:
                    if m1<len(word1):
                        rstring= rstring+(word1[m1:len(word1)])
                        return rstring
                    else:

                        return rstring
                flag = True
        return rstring