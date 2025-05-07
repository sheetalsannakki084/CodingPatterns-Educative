class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None



def buildtree(pre,ino):
    if not pre or not ino:
        return None

    rootvalue=pre[0]
    root=Node(rootvalue)
    posroot=ino.index(rootvalue)

    root.left=buildtree(pre[1:1+posroot],ino[:posroot])
    root.right=buildtree(pre[1+posroot:],ino[posroot+1:])

    return  root


def print_tree(root, level=0):
    if root is None:
        return
    print(" " * (level * 4) + "_", root.data)
    print_tree(root.left, level + 1)
    print_tree(root.right, level + 1)
#
# preorder[1:1 + posofroot]:
#
# The first element in Preorder (preorder[0]) is the root of the tree. We've already used it, so we slice it off and start with preorder[1:].
# posofroot = 3, so we are taking the first 3 elements of the remaining Preorder.
# preorder[1:1 + 3] = [2, 4, 5]
# inorder[:posofroot]:
#
# Step 1: Root of the Tree
# pre = [3, 9, 20, 15, 7], ino = [9, 3, 15, 20, 7]
# rootvalue = pre[0] = 3
# root = Node(3)
# posroot = ino.index(3) = 1 (3 is at index 1 in inorder)
# Inorder split:
# Left: ino[:posroot] = [9] (before 3)
# Right: ino[posroot+1:] = [15, 20, 7] (after 3)
# Preorder split:
# Left: pre[1:1+posroot] = pre[1:2] = [9] (1 element, matching left subtree size)
# Right: pre[1+posroot:] = pre[2:] = [20, 15, 7]






pre=[3,9,20,15,7]
ino=[9,3,15,20,7]
result=buildtree(pre,ino)
print(print_tree(result))
