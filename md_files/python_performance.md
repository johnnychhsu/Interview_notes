## Python Performance
### Why numpy array is faster than python list?
Roughly speaking, there are two reasons:
1. List can take different type of onject, and it is resizable.
2. List store pointer points to the element, where numpy array store elements diretly.

Let's take a look at how numpy array is stored in memory.

### How numpy array is stored in memory ?
It is homogenous, continuous and fixed-sized items. There two concept relating to memory: **dimension** and **strides**. <br />
Dimension is the shape of the array, like `(2,4,3)`, while strides mean the number of bytes we need to cross in each dimension. For example, if we have an array with shape `(2,3)`, dtype is int (2 bytes). Then the stride is `2 * 3 = 6 (bytes)`.
