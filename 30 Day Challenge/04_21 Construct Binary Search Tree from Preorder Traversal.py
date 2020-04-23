# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # def insert(self,i):
    #     ptr = self.val
    #     left = True
    #     while ptr:
    #         if self.val < i:
    #             ptr = ptr.left
    #         else:
    #             ptr = ptr.right
    #             left = False
    #         print(tree.val)
    #     if left:
    #         self.left = TreeNode(i)
    #     else:
    #         self.right = TreeNode(i)

class Solution:
    def bstFromPreorder(self, preorder: list) -> TreeNode:
        root = TreeNode(preorder[0])
        if preorder.__len__() == 1:
            return root
        else:
            for i in preorder[1:]:
                temp_root = root
                temp = TreeNode(i)
                while temp_root:
                    if temp_root.val > temp.val:
                        if temp_root.left:
                            temp_root = temp_root.left
                        else:
                            temp_root.left = temp
                            break
                    else:
                        if temp_root.right:
                            temp_root = temp_root.right
                        else:
                            temp_root.right = temp
                            break
        return root

obj1 = Solution()
array = [8]
print(obj1.bstFromPreorder(array))