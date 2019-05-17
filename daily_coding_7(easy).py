'''
A unival tree (which stands for "universal value") is a tree
where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
'''
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def unival(root):
    '''
    root: root node of a binary tree
    '''

    result = 0

    if root == None:
        return 0

    result += unival(root.left)
    result += unival(root.right)

    if root.left == None and root.right == None:
        return 1

    if root.left != None and root.right != None:
        if root.left.val == root.val and root.right.val == root.val:
            result += 1

    return result


# TESTCASES
root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(0, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(0))

print(unival(root)) # Should be 5
