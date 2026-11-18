# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return None

            if p.val <= node.val <= q.val or q.val <= node.val <= p.val:
                return node
            elif dfs(node.left):
                return dfs(node.left)
            elif dfs(node.right):
                return dfs(node.right)
            else:
                return None
        
        return dfs(root)
