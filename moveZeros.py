from collections import Counter
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        countzero = Counter(nums)
        numZero = 0
        for value, occ in countzero.items():    
            if value == 0:
                numZero = occ
        nums[:] = (value for value in nums if value != 0)
        while(numZero != 0):
            nums.append(0)
            numZero = numZero - 1