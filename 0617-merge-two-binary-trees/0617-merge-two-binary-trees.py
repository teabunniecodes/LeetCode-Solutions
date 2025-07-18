# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.find_merge_node(root1, root2)
        
    def find_merge_node(self, node1, node2):
        if (node1 is None and node2 is None) or (node1 and node2 is None):
            return node1
        elif node1 is None and node2:
            return node2
        elif node1 and node2:
            node1.val += node2.val
            node1.left = self.find_merge_node(node1.left, node2.left)
            node1.right = self.find_merge_node(node1.right, node2.right)
        return node1