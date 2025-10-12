#THIS CODE IS RELATED TO PROBLEM 543. Diameter of Binary Tree IN LEETCODE
#BELOW IS THE PROBLEM STATEMENT FOR REFERENCE
#TOPIC: DFS
'''Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            if not node: #if node is null there is no depth
                return 0
            l = dfs(node.left) #calc left side of node
            r = dfs(node.right) #calc right side of node
            nonlocal res
            res = max(res, l+r) #l+r because that will find the longest subtree
            return 1 + max(l, r)
        dfs(root)
        return res
