## Built-in function
### Filter
```python
def isOdd(n):
    if n % 2 == 1:
        return True
    else:
        return False
a = [1,2,3,4,5,6,7]
tmp = filter(isOdd, a)
ans = list(tmp)
```
