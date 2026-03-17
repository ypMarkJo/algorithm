class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ret=defaultdict(list)
        for s in strs:
            ret["".join(sorted(s))].append(s)
        return list(ret.values())