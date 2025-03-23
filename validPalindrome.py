class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        check = ""
        for i in s:
            if i.isalpha() or i.isnumeric():
                check = check+i
        check = check.lower()
        return check == check[::-1]