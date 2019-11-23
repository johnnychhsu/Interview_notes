## Linux
### Init system
#### System V
We can use 
```
service --status-all
```
to check running deamon.

#### System d
We can use
```
systemctl list-units --type service
```
to check running deamon.

### /dev/tty
Those device connect to our computer. We can use `2 > /dev/tty` to pass the number to our device.

### /dev/null
We can redirect error message to /dev/null, so that the error message will be missed.

### Heap and stack
#### Stack
1. Local varialbes are in stack, and those variables will be removed after the function exit. 
2. Stack is faster because it uses a pointer to push and pop data.
3. Data structure in stack can not be resized.
4. Appropriate for small data, and data that will not need to be resized.


#### Heap
1. Slower than stack.
2. We use malloc(), free() to manage data in heap. Programmers need to maintain the memory management theirselves. Be careful about memory leak.
3. There might be memory segmentation problem once we allocate and free memory many times.
4. We can resize data in heap.
