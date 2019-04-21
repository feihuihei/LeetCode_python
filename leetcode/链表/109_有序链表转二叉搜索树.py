# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        if not head or not head.next:
            return None if not head else TreeNode(head.val)
        #快慢指针找链表中点
        pre = head
        mid = head
        beh = head
        while beh and beh.next:
            pre = mid
            mid = mid.next
            beh = beh.next.next
        pre.next = None #这里将链表从中间截断
        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root