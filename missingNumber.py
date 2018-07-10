class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp_sum = len(nums)*(len(nums)+1)/2
        t_sum = sum(nums)
        return temp_sum - t_sum

