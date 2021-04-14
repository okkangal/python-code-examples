>>> def f(x, y):
...     return x + y
...

>>> from functools import reduce
>>> reduce(f, [1, 2, 3, 4, 5], 100)  # (100 + 1 + 2 + 3 + 4 + 5)
115

>>> # Using lambda:
>>> reduce(lambda x, y: x + y, [1, 2, 3, 4, 5], 100)
11



# check the reduceexample.png for explanation 
