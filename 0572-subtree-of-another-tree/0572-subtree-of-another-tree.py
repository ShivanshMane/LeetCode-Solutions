'''
Approach - 
    We will use dfs to first check is subRoot doesen't exists, if yes, we return true
    then we check if not root and return false as there is no root 
    then we check if its same tree using isSameTree method, which will return bool
    then recursively call, isSubtree on root.left and subRoot and root.right and subRoot
    time complexity - O(n), space complexity - O(n)

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False 
        
        if self.isSameTree(root, subRoot):
            return True 
        
        return(self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,subRoot))

    def isSameTree(self, p:Optinoal[TreenNode], q: Optional[TreeNode])->bool:
        if not p and not q:
            return True 
        
        if not p or not q:
            return False
        
        if p.val!=q.val:
            return False
        
        return(self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right))
        