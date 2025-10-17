class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        remains=0
        split=0
        for i in range(len(s)):
                if s[i]=='R':
                    remains+=1
                else:
                    remains-=1

                if remains==0:
                    split+=1
                              
        return split
