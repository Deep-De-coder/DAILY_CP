# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Base condition...
        if len(nums) == 0:
            return None
        # set the middle node...
        mid = len(nums)//2
        # Initialise root node with value same as nums[mid]
        root = TreeNode(nums[mid])
        # Assign left subtrees as the same function called on left subranges...
        root.left = self.sortedArrayToBST(nums[:mid])
        # Assign right subtrees as the same function called on right subranges...
        root.right = self.sortedArrayToBST(nums[mid+1:])
        # Return the root node...
        return root


'''
We need to keep track of two things:
1. Any node should have smaller elements as left children and vice versa for right children...
2. The BST should be Height Balanced...
Note, A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one...
'''
