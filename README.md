# Code Katas
A series of short programs in python, based on katas from Code Wars.

## Problem 1: Return Negative.
Module Name: return_negative.py
Test Module Name: test_return_negative.py
Link: https://www.codewars.com/kata/55685cd7ad70877c23000102/train/python
Best solution: 
```python
This was the solution by staticor, axwalker (plus 179 more warriors):
def make_negative(number):
    return -abs(number)
```


## Problem 2: Find Maximum and Minimum Values of a List
Module Name: minmax.py
Test Module Name: test_minmax.py
Link: https://www.codewars.com/kata/577a98a6ae28071780000989/train/python
Best solution:
```python
This was the solution by: snormandeau, Pang Wang
def m(arr):
    return min(arr)

def m(arr):
    return max(arr)
```
*Note- I did not think you could use the actual min/ max functions for this!*


## Problem 3: Even or Odd
Module Name: even_odd.py
Test Module Name: test_even_odd.py
Link: https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/train/python
Best solution:
```python
This was the solution by: laoris, colbydauph, (plus 212 more warriors)
def even_or_odd(number):
  return 'Odd' if number % 2 else 'Even'
```

## Problem 4: Convert number to reversed array of digits
Module Name: convert.py
Test Module Name: test_convert.py
Link: https://www.codewars.com/kata/convert-number-to-reversed-array-of-digits/train/python
Best solution:
```python
This was the solution by: colbydauph, vishnub (plus 58 more warriors)
def digitize(n):
    return map(int, str(n)[::-1])
```

## Problem 5: Sum of Positive
Module Name: sum_positive.py
Test Module Name: test_sum_positive.py
Link: https://www.codewars.com/kata/sum-of-positive/train/python
Best Solution:
```python
This was the solution by: lancelote, CrazyMerlyn (plus 56 more warriors)
def positive_sum(arr):
    return sum(x for x in arr if x > 0)
```



