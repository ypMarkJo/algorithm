class RecentCounter(object):

    def __init__(self):

        self.recents=[]

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        if t:
            self.recents.append(t)
            end=len(self.recents)-1
            i=end
            while i>=0 and t-3000 <= self.recents[i]<=t:
                i-=1
                
        return end-i
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)