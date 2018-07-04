from collections import Counter
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        returnVal = 0
        largestCount = 0
        print(count)
        for value, occ in count.items():    
            if occ > largestCount:
                largestCount = occ
                returnVal = value
        return returnVal