## Algorithm 

### Doubly linked list
We can use only one pointer to save the next and previous node information. We only need to save the xor result of the next node address and previous node address.
```c++
typedef int T;
typedef struct listNode{
    T elm;
    struct listNode * ptrdiff;
};
```
In this case, we can start traversal from head or tail. Each time we xor with the previous node, then we can get the address of next node.

#### Reference
1. [A memory efficient doubly linked list](https://www.linuxjournal.com/article/6828)

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

### Find median between 3 numbers using only 2 comparison
First we pick two number from the list, 
```python
arr = [a, b, c]

# Choose two, subtract them using the left one
x = a - b
y = a - c

# Suppose x, y both > 0, we choose the bigger one between b and c
# Suppose x, y both < 0, we choose the smaller one between b and c
# Suppose x > 0, y < 0, we choose a
# Suppose x < 0, y > 0, we choose a
```

### Pattern Matching : KMT Algorithm
```python
def KMPSearch(pat, txt): 
    M = len(pat) 
    N = len(txt) 
  
    # create lps[] that will hold the longest prefix suffix  
    # values for pattern 
    lps = [0]*M 
    j = 0 # index for pat[] 
  
    # Preprocess the pattern (calculate lps[] array) 
    computeLPSArray(pat, M, lps) 
  
    i = 0 # index for txt[] 
    while i < N: 
        if pat[j] == txt[i]: 
            i += 1
            j += 1
  
        if j == M: 
            print "Found pattern at index " + str(i-j) 
            j = lps[j-1] 
  
        # mismatch after j matches 
        elif i < N and pat[j] != txt[i]: 
            # Do not match lps[0..lps[j-1]] characters, 
            # they will match anyway 
            if j != 0: 
                j = lps[j-1] 
            else: 
                i += 1
  
def computeLPSArray(pat, M, lps): 
    len = 0 # length of the previous longest prefix suffix 
  
    lps[0] # lps[0] is always 0 
    i = 1
  
    # the loop calculates lps[i] for i = 1 to M-1 
    while i < M: 
        if pat[i]== pat[len]: 
            len += 1
            lps[i] = len
            i += 1
        else: 
            # This is tricky. Consider the example. 
            # AAACAAAA and i = 7. The idea is similar  
            # to search step. 
            if len != 0: 
                len = lps[len-1] 
  
                # Also, note that we do not increment i here 
            else: 
                lps[i] = 0
                i += 1
  
txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
KMPSearch(pat, txt) 
  
# This code is contributed by Bhavya Jain 
```

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

### How to prove DP algorithm
1. Define sub-problem
2. Present the recurrence
3. Justify it is correct
4. State base case
5. Present the algorithm
6. Time and space complexity

### Loop Invariance
To prove a computer program, there are two corectness.
1. Partial correctness : If an answer is returned, it is correct
2. Total correctness : The program terminate

Due to halting problem, total correctness is not decidible. We can prove the partial correctness by loop invariance. <br />
The loop invariance hold for precondition, after each iteration and after exiting the loop. <br />
The postconsition can be as a composition as invariance and exiting condition. We need to find some previous state that holds the loop invariance, but slightly away from the exiting condition. Accordingly, we need to find a initial state that holds the invariance as the init of the algorithm.

#### Reference
1. [Loop Invariance Paper](https://arxiv.org/pdf/1211.4470.pdf)
2. [Partial Correctness of computer program](https://medium.com/@tranduchanh.ms/partial-correctness-of-computer-program-f541490e7a21)
3. [Loop Invariance Video](https://www.youtube.com/watch?v=3YP6NP1_tF0)

#### Reference
1. [DP Prove Steps](https://www.cs.oberlin.edu/~asharp/cs280/2012fa/handouts/dp.pdf)
