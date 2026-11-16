# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Understanding the problem = 
    Input - we have the root of the binary search tree, integer k
    Goal - return the kth smallest value from all the values from the binary search tree
    Ouput - return the smallest value 

Constraints =
    what if not root
    what is the max number of nodes in the bst 
    can the bst be skewed 

Examples =  
         = Input: root = [2,1,3], k = 1, Output: 1
         = Input: root = [4,3,5,2,null], k = 4, Output: 5

Approach = 
    we can use the dfs algorithm to traverse through the bst side wise, first left side of tree, then right side 
    use a stack to store which nodes do we need to visit
    Go left
    Push every node into the stack until you cannot go left anymore.
    Visit the leftmost node
    Pop it from the stack and decrease k.
    Check k
    If k = 0, return the current node's value.
    Explore right
    Move to the right child, and repeat the process.
    If curr is None
    Return to the next parent node using the stack
    Time complexity - O(n), space complexity - O(n)
'''
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
        