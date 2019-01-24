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

### Convert decimal to hexadecimal
First convert `n` into binary form. For example, `29 -> 00011101`. Then, group every four bits together. Convert each group into decimal, then convert it to hexadecimal. Then we get the answer. <br />
To get the digit for each group, we can do `&` with 15, which is `1111` in binary. Then we get the digit for this group in hexadecimal. Next, we do `n >>= 4`, then do the same thing again.

### Implement queue in Python
```python
class Queue():
    def __init__(self):
        self.queue = []    

    def enqueue(self, x):
        self.queue.insert(0, x)

    def dequeue(self):
        self.queue.pop()
```
### Min Heap Implementation in Python
[Min Heap](./myheap.py)

### A\*



