## Decorator
Function decorators are simply wrapper for function. Bwlow are some facts that help to understand decorator : 

1. Function can be passed as a parameter
2. Function can return other function
3. Inner function have access to the encoding scope (closure)
    ```python
    def compose_greet_func(name):
        def get_message():
            return "Hello there "+name+"!"

        return get_message

    greet = compose_greet_func("John")
    print(greet())

    # Outputs: Hello there John!
    ```

### Example
**Composition of decorator** <br />
```python
def get_text(name):
   return "lorem ipsum, {0} dolor sit amet".format(name)

def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

my_get_text = p_decorate(get_text)

print(my_get_text("John"))

# <p>Outputs lorem ipsum, John dolor sit amet</p>
```
This is our first decorator! A function that takes another function as an argument, generate a new function, and return the generated function.<br />
To have get_text decirated by p_decorated, we can simply
```python
get_text = p_decorated(get_text)
```
Then `get_text` is augmented by `p_decorated` and can be used anywhere.

### Python Syntax
We don't need to do the previous assignment, we can simply use @ symbol to decorate.
```python
def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

@p_decorate
def get_text(name):
   return "lorem ipsum, {0} dolor sit amet".format(name)

print(get_text("John"))

# Outputs <p>lorem ipsum, John dolor sit amet</p>
```

We can pass arguments to decorator : 
```python
def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator

@tags("p")
def get_text(name):
    return "Hello "+name

print(get_text("John"))

# Outputs <p>Hello John</p>
```
The reason we need one more layer in the decorator is : <br />
We want the decorator to return an augmented function, thus we need a inner function, then return it. If we want to pass value into decorator, then we need one more function to accpet the parameter. 
<br />
If we don't use the @ symbol, instead write it ourself, then we don't need the outter layer.

**Other things to note** <br />
After we decoarte a function, the attributes like `__name__`, `__doc__` of the original function are overridden by the decorator. This may lead to some problems when debugging. To solve this issue, we can use `functools.wraps` : 
```python
from functools import wraps

def tags(tag_name):
    def tags_decorator(func):
        @wraps(func)
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator

@tags("p")
def get_text(name):
    """returns some text"""
    return "Hello "+name

print(get_text.__name__) # get_text
print(get_text.__doc__) # returns some text
print(get_text.__module__) # __main__
``` 

### Real Example
```python
import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])
```

### Reference
1. [Python Decorator](https://www.thecodeship.com/patterns/guide-to-python-function-decorators/)
2. [More detail about decorator](https://realpython.com/primer-on-python-decorators/#syntactic-sugar)
