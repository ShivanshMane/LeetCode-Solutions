'''
Understanding the problem - 
    Input - we have root of a binary tree
    Goal - invert the binary tree by swapping left and right children
    Output - return the root of the inverted binary tree 

Constraints - 
    what if the root is None
    can the tree contain only 1 node
    can the tree contain duplicates 
    can the tree have negative values or zero
    what is the maximum number of nodes

Examples -
    Input: root = [2,1,3], Output: [2,3,1]
    Input: root = [], Output: []

Approach - 
    We can iterate through the tree using dfs(depth first search algorithm), which first checks the left part of tree and then the right part 
    Using this algorithm we can iterate through the left children of root, swap them 
    then recursively call, the same function on its left children 
    and then right children 
    can return the current root
    time complexity - O(n), space complexity - O(n)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        # base case
        if not root:
            return None
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root