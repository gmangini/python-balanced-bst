from binarysearchtree import BinarySearchTree

def main():

    tree = BinarySearchTree()
    tree.add(10)
    tree.add(8)
    tree.add(6)
    tree.add(12)
    tree.add(11)
    tree.add(11)

    print(tree.preorder())
    print(tree.inorder())
    print(tree.rebalance_tree())


if __name__ == "__main__":
    main()
