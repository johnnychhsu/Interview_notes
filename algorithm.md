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
A\* is the most popular algorithm for path finding.
1. A\* is like Dijkstra that it can be used to find a shortest path
2. A\* is like greedy Best First Search that it can use a heuristic to guide
It consider both the distance from starting point and distance from goal. <br />
**Heuristic** <br />
Trade between accuracy and speed. Heuristic value compared to the true value leads to different result.
1. If heuristic lower, then A\* is more similar to Dijkstra.
2. If it is higher, then it is more similar to greedy best first search.

```python
def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current
    
    return came_from, cost_so_far

def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start) # optional
    path.reverse() # optional
    return path
```
#### Reference
[A\* Algorithm](http://theory.stanford.edu/~amitp/GameProgramming/ImplementationNotes.html)

