# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Approach - 
    We need to create a helper function valid, as the main function returns the bool 
    then check if the node is none, if yes return None 
    then check if left < node.val < right(initially the left will be -ve infinity and right will be +ve infinity)
    then recursivley call valid on left, by node.left, left, node.val
    and on the right, by node.right, node.val, right
    then return the valid with root(main function), - ve inf, and + ve inf
'''
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            
            if not (left< node.val < right):
                return False
            
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)

        return valid(root, float("-inf"), float("+inf"))
        