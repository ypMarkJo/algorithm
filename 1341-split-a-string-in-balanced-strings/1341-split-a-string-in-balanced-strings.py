class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        remains=0
        split=0
        i=0
        while i < len(s)-1:
            print(s[i]+","+s[i+1]+",remains: ",remains,",split: ",split)
            if s[i]==s[i+1]:
                if s[i+1]=='R':
                    remains+=1
                else:
                    remains-=1
                if remains==0:
                    split+=1
                    i+=1

            elif s[i]!=s[i+1]:
                if remains==0:
                    split+=1
                    i+=1
            i+=1        
                    
        return split
