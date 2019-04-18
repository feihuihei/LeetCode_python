# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def inorderTraversal(self, root):
        if not root:
            return []

        arr = []
        stack = []
        node = root
        while stack or root:

            while node:
                stack.append(node)
                node = node.next
            node = stack.pop()
            arr.append(node.val)
            node = node.right
        return arr
    #每个节点儿右向指针
    def connect(self, root):
        if root is None:
            return None
        if root.left:
            root.left.next = root.right
            if root.next != None:
                root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
    #根据前序遍历和中序遍历结果构建二叉树
    def buildTree(self, preorder, inorder):
        if len(preorder) ==0 or len(inorder) == 0:
            return None
        root = TreeNode(preorder[0])
        index = inorder.index(root.val)
        rightarr = inorder[index+1:]
        root.left = self.buildTree(preorder[1:index+1],inorder[0:index])
        root.right = self.buildTree(preorder[index+1:],inorder[index+1:])
        return root