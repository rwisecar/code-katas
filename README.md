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

## Problem 6: Jenny's Secret Message
Module Name: jenny.py
Test Module Name: test_jenny.py
Link: https://www.codewars.com/kata/jennys-secret-message/train/python
Best Solution:
```python
This was the solution by: mortonfox, jolaf, bkaes (plus 641 more warriors)
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)
```

## Problem 7: Sum without highest and lowest number
Module Name: sum_highlow.py
Test Module Name: test_sum_highlow.py
Link: https://www.codewars.com/kata/sum-without-highest-and-lowest-number/train/python
Best Solution:
```python
This was the solution by: eqlion
def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)
```

## Problem 8: Count the Monkeys
Module Name: monkey.py
Test Module Name: text_monkey.py
Link: https://www.codewars.com/kata/56f69d9f9400f508fb000ba7/train/python
Best Solution:
```python
This was the solution by: Nestorfish, VadimPopov (plus 236 more warriors)
def monkey_count(n):
    return range(1, n+1)
```

## Problem 9: Alternating Case
Module Name: alt_case.py
Test Module Name: test_altcase.py
Link: https://www.codewars.com/kata/alternating-case-%3C-equals-%3E-alternating-case/train/python
Best Solution:
```python
This was the solution by: Nestorfish, Demon Slayer (plus 147 more warriors)
def to_alternating_case(string):
    return string.swapcase()
```

## Problem 10: Grade Book
Module Name: get_grade.py
Test Module Name: test_grade.py
Link: https://www.codewars.com/kata/grasshopper-grade-book/train/python
Best Solution:
```python
This was the solution by acaccia:
def get_grade(s1, s2, s3):
    return {6:'D', 7:'C', 8:'B', 9:'A', 10:'A'}.get((s1 + s2 + s3) / 30, 'F')
```

## Problem 11: Convert a String to a Number
Module Name: string2num.py
Test Module Name: test_string2num.py
Link: https://www.codewars.com/kata/convert-a-string-to-a-number/train/python
Best Solution:
```python
This was the solution by warwickwang (plus 1307 more warriors)
def string_to_number(s):
    return int(s)
```

## Problem 12: Do I Get a Bonus?
Module Name: fatcat.py
Test Module Name: test_fatcat.py
Link: https://www.codewars.com/kata/do-i-get-a-bonus/train/python
Best Solution:
```python
This was the solution by zebulan, ChristianECooper, AbuBakar2001, christoph531, tedmiston
def bonus_time(salary, bonus):
    return "${}".format(salary * (10 if bonus else 1))
```

## Problem 13: Find the Next Perfect Sq (7kyu)
Module Name: next_sq.py
Test Module Name: test_nextsq.py
Link: https://www.codewars.com/kata/find-the-next-perfect-square/train/python
Best Solution:
```python
This was the solution by Beast, nicolasreymond
def find_next_square(sq):
    x = sq**0.5
    return -1 if x % 1 else (x+1)**2
```