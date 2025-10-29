class RecentCounter(object):

    def __init__(self):

        self.recents=deque()

    # def ping(self, t):
    #     """
    #     반복문 방식
    #     :type t: int
    #     :rtype: int
    #     """
    #     if t:
    #         self.recents.append(t)
    #         end=len(self.recents)-1
    #         i=end
    #         while i>=0 and t-3000 <= self.recents[i]<=t:
    #             i-=1
                
    #     return end-i
    
    def ping(self, t):
        """
        첫항 삭제 방식
        :type t: int
        :rtype: int
        """
        self.recents.append(t)
        while self.recents[0]<t-3000:
            # del self.recents[0]
            # del < popleft() 성능이네
            self.recents.popleft()
        return len(self.recents)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)