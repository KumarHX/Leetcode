# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def merge_lists(self, h1, h2):
        if h1 is None:
            return h2
        if h2 is None:
            return h1

        if (h1.val < h2.val):
            h1.next = self.merge_lists(h1.next, h2)
            return h1
        else:
            h2.next = self.merge_lists(h2.next, h1)
            return h2
        
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge_lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists

    