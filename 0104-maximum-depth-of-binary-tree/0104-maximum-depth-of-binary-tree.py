'''
Understanding the problem - 
    Input - gievn the root of a binary tree 
    Goal - find the maximum depth of the binary tree
    Output - return the maximum depth of that binary tree

Constraints - 
    what if the root is none 
    can the binary tree have only one node
    can the tree have only one side 
    what id the maximum number of nodes
    is there any restriction on node values

Examples - 
    Input: root = [3,9,20,null,null,15,7], Output: 3
    Input: root = [1,null,2], Output: 2
    Input: root = [3], Output: 1
    Input: root = [], Output: 0

Approach - 
    - we can use the dfs algorithm here to traverse through the tree, side by side, left first and then right 
    - first we can check the base case which is what if the root is null or not root
    - then we can recrusivley call teh function on the left side, and then right side 
    - and we can create two, leftDepth = maximum depth of the left subtree rightDepth = maximum depth of the right subtree
    - then leftDepth return the value of left hand side starting from the bottom, same for right side
    - return 1 + max(leftdepth, rightdepth)
    1 is beacuse root is also counted 
    time complexity - O(n), space complexity - O(n)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)