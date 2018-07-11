from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        values = []
        count = Counter(nums)
        for val, occ in count.items():
            if(occ == 1):
                values.append(val)
        return values
        