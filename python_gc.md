## Python memory management and garbage collection

Everything in Python is object. The Cython implementation use Pyobject to describe everything in Python. This type of object contains two things:

1. ob_refcnt: reference count
2. ob_type: pointer to another type

The reference count is used for garbage collection. Each time assign an object, the count increase one. When it drops to zero, means that we can free the memory space for other usage.

Some example about the count :
```python
numbers = [1, 2, 3]
# Reference count = 1
more_numbers = numbers
# Reference count = 2

total = sum(numbers)
# Reference count = 3
```


