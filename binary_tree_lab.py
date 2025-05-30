from typing import Optional

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

# Function to compute the max depth of the binary tree
def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return max(max_depth(root.left), max_depth(root.right)) + 1

# Function to find the lowest common ancestor in a BST
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root:
        return None

    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)
    elif p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)

    return root  # If split occurs, root is the LCA