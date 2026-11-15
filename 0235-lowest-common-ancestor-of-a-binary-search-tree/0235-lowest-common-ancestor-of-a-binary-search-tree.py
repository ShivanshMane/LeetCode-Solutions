# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Understanding the problem -     
    Input = a binary search tree
    Goal = to find the lowest common ancestor node in the BST
    Output = return the lowest common ancestor
Constraints - 
    what if the the root is None
    number of nodes in the tree
    are both p and q guaranteed to exists in the tree 
    can p and q be the same node 
Examples - 
    root = [3,5,1,6,2,0,8,null,null,7,4]
      p = 5, q = 1
      Output = 3
   2. root = [3,5,1,6,2,0,8,null,null,7,4]
      p = 5, q = 4
      Output = 5
   3. root = [1,2]
      p = 1, q = 2
      Output = 1
   4. root = [1,2,3]
      p = 2, q = 3
      Output = 1
   5. root = [1,2,null,3,null,4]
      p = 3, q = 4
      Output = 3
Approach - 
    We could use the dfs algortihm to traverse through the tree
    first check if the root is none, if yes return None
    check if the root is equal to p or q, if yes return root
    then recursively check left tree, with paramaters,root.left,p,q and store the result in left 
    do the same for right side with parameters, root.right,p, q and store result in right
    then check if left and right are not none, return the root
    time complexity - O(n), space complexity - O(n)
'''
class Solution:
    def lowestCommonAncestor(self, root: Optiona[TreeNode], p:Optional[TreeNode], q:Optional[TreeNode])->TreeNode:
        if not root:
            return None
        
        if p == root or q == root:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right,p, q)

        if left and right:
            return root

        return left or right