class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        setted=set(s)
        for letter in setted:
            if s.count(letter)!=t.count(letter):
                return False
        if len(s)==len(t): 
            return set(s)==set(t)
        else: 
            return False