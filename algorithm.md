## Algorithm 

### Trie
1. Used for prefix search.

### Segment Tree
1. Compressed Trie.
2. It is used when we need to find Maximum/Minumum/Sum/Product of numbers in a range.

### Binary Tree Traversal
1. Inorder : (Left, Root, Right)
2. Preorder : (Root, Left, Right)
3. Postorder : (Left, Right, Root)

Usually we use a stack or recurrsion to do this. But we can use Morris traversal without those two methods. <br />
```python
current = root
while current:
    if not current.left:
        print(current.val)
        current = current.right
    else:
        predecessor = findMaxInLeftsubtree(current)
        if not predecessor.right:
            predecessor.right = current
            current = current.left
        else:
            predecessor.right = None
            print(current)
            current = current.right
```
<br />
The idea is to connect the largest element in the left sub-tree back to the root. Then after we traversal all nodes in left sub-tree, we can go back to root, then start to traversal right sub-tree.
