# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        lh = 0
        node = root;
        while(node != None):
            lh += 1
            node = node.left
        rh = 0
        node = root
        while(node != None):
            rh += 1
            node = node.right
        if lh == rh:
            return pow(2, lh) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)