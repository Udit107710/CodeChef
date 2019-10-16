#Question: https://leetcode.com/problems/binary-tree-inorder-traversal/

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            sol = []
            if root.left:
                left = self.inorderTraversal(root.left)
                sol.extend(left)
            sol.append(root.val)
            if root.right:
                right = self.inorderTraversal(root.right)
                sol.extend(right)
            return sol       
        else:
            return []
    