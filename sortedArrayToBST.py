# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
 
        # find middle
        mid = (len(nums)) / 2

        # make the middle element the root
        root = TreeNode(nums[mid])

        # left subtree of root has all
        # values <arr[mid]
        root.left = self.sortedArrayToBST(nums[:mid])

        # right subtree of root has all 
        # values >arr[mid]
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root