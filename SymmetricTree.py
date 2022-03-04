# TC : O(n); n is no.of nodes
# SC : O(h); h is the height of tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if (not root):
            return True
        
        def isSymmetrical(act, mir):
            if(not act and not mir):
                return True
            
            if(not act or not mir or act.val!= mir.val):
                return False
            
            return isSymmetrical(act.left, mir.right) and isSymmetrical(act.right, mir.left)
    
        return isSymmetrical(root.left, root.right)
