class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if  not root:
            return res
        queue = []
        queue.append(root)
        level = 0
        while len(queue) > 0:
            n = len(queue)
            temp = []
            if level % 2 == 0:
                for i in range(n):
                    cur = queue.pop(n-i-1)
                    temp.append(cur.val)
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
            else:
                for i in range(n):
                    cur = queue.pop(n-i-1)
                    temp.append(cur.val)
                    if cur.right:
                        queue.append(cur.right)
                    if cur.left:
                        queue.append(cur.left)
            res.append(temp)
            level += 1
        return res
    #获取二叉树的最大宽度 leetcode662
    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        Max = 0
        queue = [(root, 0)]
        while queue:
            size = len(queue)
            LEN = queue[-1][1] - queue[0][1] + 1
            Max = max(Max, LEN)
            for i in range(size):
                node = queue.pop(0)
                if node[0].left:
                    queue.append((node[0].left, 2 * node[1]))
                if node[0].right:
                    queue.append((node[0].right, 2 * node[1] + 1))
        return Max

        #二叉树的层序遍历 102
    #二叉树的层序遍历
    def levelOrder(self, root):
        if not root:
            return []
        queue = [root]
        arr = []
        while queue:
            temp =[]
            for i in range(len(queue)):
                root = queue.pop(0)
                temp.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            arr.append(temp)
        return arr
    #二叉树转化为链表
    def flatten(self, root):
        if not root:
            return None
        if root.left == None and root.right == None:
            return None
        self.flatten(root.left)
        self.flatten(root.right)
        tmp = root.right
        root.right = root.left
        root.left = None
        while root.right:
            root = root.right
        root.right = tmp
    #删除二叉搜索树中的节点
    def deleteNode(self, root, key):
        if not root:
            return None
        if root.val > key:
            self.deleteNode(root.left,key)
        elif root.val < key:
            self.deleteNode(root.right,key)
        else:
            if root.left == None or root.right == None:
                root = root.left if not root.left else root.right
            else:
                cur = root.right
                while cur.left:
                    cur = cur.left
                root.val = cur.val
                root.right = self.deleteNode(root.right,cur.val)
        return root

    #从二叉搜索树中查找需要删除的节点
    def deleteNode(self, root, key):
        if not root: return None;
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left or not root.right:
                root = root.left if root.left else root.right
            else:
                cur = root.right
                while cur.left:
                    cur = cur.left
                root.val = cur.val
                root.right = self.deleteNode(root.right, cur.val)
        return root;

root = TreeNode(1)
root.left = a = TreeNode(3)
root.right = b = TreeNode(2)
a.left = c =TreeNode(5)
c.left =TreeNode(6)
b.right = TreeNode(9)
b.right.right = TreeNode(7)


obj = Solution()
print(obj.widthOfBinaryTree(root))