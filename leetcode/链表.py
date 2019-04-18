# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    #两个链表做相加 （但是会超时）
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        flag = False
        head = ListNode(0)
        pre = head
        while l1 and l2:
            sum = l1.val + l2.val
            if flag:
                sum += 1
                if sum >= 10:
                    node = ListNode(sum%10)
                    pre.next = node
                    flag = True
                else:
                    node = ListNode(sum)
                    pre.next = node
                    flag = False
            else:
                if sum >= 10:
                    node = ListNode(sum%10)
                    pre.next = node
                    flag = True
                else:
                    node = ListNode(sum)
                    pre.next = node
                    flag = False
            l1 = l1.next
            l2 = l2.next
            pre = pre.next
        end = None
        if l1:
            end = l1
        else:
            end = l2
        while end:
            if flag:
                sum = end.val+1
                if sum >= 10:
                    node = ListNode(sum%10)
                    pre.next = node
                    flag = True
                else:
                    pre.next = ListNode(end.val+1)
                    end = end.next
                    pre = pre.next
                    flag = False
            else:
                pre.next = end
                break
        if not end:
            if flag:
                pre.next = ListNode(1)
        return head.next

    #找两个相交链表的节点
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        m ,n = 0,0
        pre = headA
        while pre:
            m += 1
            pre = pre.next
        pre = headB
        while pre:
            n += 1
            pre = pre.next
        if m >= n:
            for i in range(m-n):
                headA = headA.next
        else:
            for i in range(n-m):
                headB = headB.next
        while headA and headB:
            if headA.val == headB.val:
                return headA
            else:
                headA = headA.next
                headB = headB.next
