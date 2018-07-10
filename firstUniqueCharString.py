from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = Counter(s)
        for val in s:
            if(count.get(val) == 1):
                return s.find(val)
        return -1
        