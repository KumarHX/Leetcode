from collections import Counter
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        print(count)
        for value, occ in count.items():    
            if occ == 1:
                return value
        return null
        