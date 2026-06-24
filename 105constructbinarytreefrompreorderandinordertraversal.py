# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def build(self, left_idx, right_idx):
        if left_idx > right_idx:
            return None
        
        root_val = self.preorder[self.inorder_root_idx]

        preorder_root_idx = self.lkup[root_val]#elf.find_root_idx(root_val, left_idx, right_idx)

        if preorder_root_idx == -1:
            return None

        tree_node = TreeNode(root_val)
        self.inorder_root_idx += 1

        tree_node.left = self.build(left_idx, preorder_root_idx - 1)

        tree_node.right = self.build(preorder_root_idx + 1, right_idx)

        return tree_node


    def find_root_idx(self, val, left_idx, right_idx):
        for each_idx in range(left_idx, right_idx + 1):
            if self.inorder[each_idx] == val:
                return each_idx
        
        return -1


    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
            The crux of the problem is understanding the formation of tree from inorder and preorder traversal.
            Note that for any root, the left half of its inorder traversal will be its left subtree.
            The right half will its right subtree.
            In this manner we start with the 0 index and then move in the inorder one by one and then assign the nodes.
            In this way we form the tree and return it.
        """
        left_idx = 0
        right_idx = len(preorder) - 1
        self.lkup = {}

        self.inorder_root_idx = 0

        self.preorder = preorder
        self.inorder = inorder

        for each_idx in range(len(self.preorder)):
            self.lkup[self.inorder[each_idx]] = each_idx

        return self.build(left_idx, right_idx)

"""
class Solution:

    def build(self, left_idx, right_idx):
        if left_idx > right_idx:
            return None
        
        root_val = self.preorder[self.inorder_root_idx]

        preorder_root_idx = self.find_root_idx(root_val, left_idx, right_idx)

        if preorder_root_idx == -1:
            return None

        tree_node = TreeNode(root_val)
        self.inorder_root_idx += 1

        tree_node.left = self.build(left_idx, preorder_root_idx - 1)

        tree_node.right = self.build(preorder_root_idx + 1, right_idx)

        return tree_node


    def find_root_idx(self, val, left_idx, right_idx):
        for each_idx in range(left_idx, right_idx + 1):
            if self.inorder[each_idx] == val:
                return each_idx
        
        return -1


    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        left_idx = 0
        right_idx = len(preorder) - 1

        self.root_idx = 0

        self.preorder = preorder
        self.inorder = inorder

        return self.build(left_idx, right_idx)
"""
