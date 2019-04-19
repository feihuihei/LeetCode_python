# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        if not head or m >= n :
            return head
        num = 1
        root = ListNode(0)
        root.next = head
        pre = root
        while pre.next and num < m:
            pre = pre.next
            num += 1
        if num < m:
            return head
        node = pre.next
        cur = node.next
        while cur and num < n :
            next = cur.next
            cur.next = pre.next
            pre.next = cur
            node.next = next
            cur = next
            num += 1
        return root.next

    #反转链表
    def reverseLinklist(self, head):
        if not head or not head.next:
            return head
        pre = None
        cur = head
        next = cur.next
        while next:
            cur.next = pre
            pre = cur
            cur = next
            next = next.next
        cur.next = pre
        return cur

    #快慢指针查找环的入口
    def detectCycle(self, head):
        if not head or not head.next or not head.next.next:
            return None
        slow = head.next
        fast = head.next.next
        while fast != slow:
            if fast.next != None and fast.next.next != None:
                fast = fast.next.next
                slow = slow.next
            else:
                return None
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow

    #链表环的长度
    def cycleLength(self,head):
        if not head or not head.next or not head.next.next:
            return None
        start = self.detectCycle(head)
        if not start:
            return 0
        next = start.next
        count = 1
        while next != start:
            count += 1
            next = next.next
        return count
    #删除链表的倒数第N个节点
    def removeNthFromEnd(self, head, n):
        if not head or n <= 0:
            return head
        pre = ListNode(0)
        pre.next = head
        cur = pre
        m = 0
        while cur:
            m += 1
            cur = cur.next
        if m < n+1 : return head
        index = 1
        temp = pre
        while index < m - n:
            index += 1
            temp = temp.next
        cur = temp.next
        temp.next = cur.next
        return pre.next
    #将链表按照数组打印
    def printLinkList(self,head):
        if not head:
            print("LinkList is Null.....")
        if self.detectCycle(head):
            print("LinkList has cycle .......")
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        print(arr)
    #给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
    def rotateRight(self, head, k):
        if not head:
            return None
        if k == 0:
            return head
        pre = ListNode(0)
        cur = head ; m = 0
        while cur:
            m += 1
            cur = cur.next
        n = k % m
        if n == 0:
            return head
        cur = head
        count = 1
        while count < m-n:
            count += 1
            cur = cur.next
        temp = pre.next = cur.next
        cur.next = None
        while temp.next:
            temp = temp.next
        temp.next = head
        return pre.next
    #给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。s
    def deleteDuplicates(self, head):
        if not head:
            return None
        pre = ListNode(0)
        pre.next = head
        node = pre
        cur = pre
        while node:
            if node.next and node.val == node.next.val:
                while node.next and node.next.val == node.val:
                    node = node.next
                cur.next = node.next
                node = node.next
            else:
                cur = node
                node = node.next
        return pre.next

    #147--对链表进行插入排序
    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        pre = ListNode("x")
        pre.next = head
        cur = head
        pp = pre
        while cur:
            last = cur.next
            if last and last.val < cur.val:
                while pp.next and pp.next.val < last.val:
                    pp = pp.next
                tmp = pp.next
                pp.next = last
                cur.next = last.next
                last.next = tmp
                pp = pre
            else:
                cur = last
        return pre.next

obj = Solution()
head = ListNode(4)
a = head.next = ListNode(2)
b = a.next = ListNode(1)
c = b.next = ListNode(3)
# d = c.next = ListNode(4)
# e = d.next = ListNode(4)
# f = e.next = ListNode(5)

obj.printLinkList(head)
node = obj.insertionSortList(head)
obj.printLinkList(node)