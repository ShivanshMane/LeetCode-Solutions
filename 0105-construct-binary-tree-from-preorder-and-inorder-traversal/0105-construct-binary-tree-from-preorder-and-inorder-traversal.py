# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        # check if not inorder and not preorder 
        if not inorder and not preorder:
            return None
        # root is always the first node in preorder list 
        root = TreeNode(preorder[0])
        # divide the list into two parts from root, left part and right part 
        mid = inorder.index(preorder[0])
        # now create the left part of tree, with everything before index 1
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid] )
        # now create the right part of the tree, with everything on the right of preorder and right of mid 
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        # return root which returns the tree
        return root