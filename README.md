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

## Problem 14: Sort Array by String Length (7kyu)
Module Name: sort_bylength.py
Test Module Name: test_sortlength.py
Link: https://www.codewars.com/kata/sort-array-by-string-length/train/python
Best Solution:
```python
This was the solution by: the_roth, iNovice_ (plus 81 more warriors)
def sort_by_length(arr):
    return sorted(arr, key=len)
```

## Problem 15: Disemvowel Trolls (7kyu)
Module Name: disemvowel.py
Test Module Name: test_disemvowel.py
Link: https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python
Best Solution:
```python
This was the solution by: cvk77, zyrolasting
def disemvowel(s):
    return s.translate(None, "aeiouAEIOU")
```

## Problem 16: Reverse Words (7kyu)
Module Name: reverse.py
Test Module Name: test_reverse.py
Link: https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python
Best Solution:
```python
This was the solution by: phatcabbage, warwickwang (plus 9 more warriors)
def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))
```

## Problem 17: Sum of First nth Term of Series
Module Name: sum_of_nth_terms.py
Test Module Name: test_sum_of_nth_terms.py
Link: http://www.codewars.com/kata/sum-of-the-first-nth-term-of-series/python
Best Solution:
```python
This was the solution by: MMMAAANNN, doctornick5, Slx64
def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
```

## Problem 18: Sorting Cards
Module Name: sort-cards.py
Test Module Name: test_sort.py
Link: https://www.codewars.com/kata/56f399b59821793533000683/
Best Solution:
```python
This was the solution by: zebulan, acaccia, j_codez, Mr.Child, iamchingel
def sort_cards(cards):
    return sorted(cards, key="A23456789TJQK".index)
```

## Problem 19: Autocomplete
Module Name: autocomplete.py
Test Module Name: test_autocomplete.py
Link: https://www.codewars.com/kata/5389864ec72ce03383000484
I originally wrote this as a code wars kata solution, but later updated it in favor of a Trie Tree implementation.
Best Solution from Code Wars:
```python
This was the solution by: s-lugo
def autocomplete(input_, dictionary):
    input_ = ''.join( [ c for c in list(input_) if c.isalpha() ])
    return [ x for x in dictionary if x.lower().startswith(input_.lower()) ][:5]
```

#*Test Coverage*

```
---------- coverage: platform darwin, python 2.7.10-final-0 ----------
Name                           Stmts   Miss  Cover   Missing
------------------------------------------------------------
src/alt_case.py                    2      0   100%
src/convert.py                     3      0   100%
src/disemvowel.py                  3      0   100%
src/even_odd.py                    4      0   100%
src/fatcat.py                      2      0   100%
src/get_grade.py                  11      0   100%
src/jenny.py                       4      0   100%
src/minmax.py                      8      0   100%
src/monkey.py                      2      0   100%
src/next_sq.py                     6      0   100%
src/parenthetics.py               45      3    93%   39, 68, 70
src/return_negative.py             2      0   100%
src/reverse.py                     2      0   100%
src/sort_bylength.py               2      0   100%
src/sort_cards.py                  7      0   100%
src/string2num.py                  2      0   100%
src/sum_highlow.py                 4      0   100%
src/sum_of_nth_terms.py            5      0   100%
src/sum_positive.py                4      0   100%
src/test_altcase.py               13      0   100%
src/test_convert.py                5      0   100%
src/test_disemvowel.py             6      0   100%
src/test_even_odd.py               5      0   100%
src/test_fatcat.py                13      0   100%
src/test_grade.py                 24      0   100%
src/test_jenny.py                  5      0   100%
src/test_minmax.py                22      0   100%
src/test_monkey.py                11      0   100%
src/test_nextsq.py                16      7    56%   26-27, 32-36
src/test_parenthetics.py          81      0   100%
src/test_return_negative.py       12      0   100%
src/test_reverse.py                6      0   100%
src/test_sort.py                  15      5    67%   28-32
src/test_sortlength.py            15      0   100%
src/test_string2num.py            10      0   100%
src/test_sum_highlow.py           14      0   100%
src/test_sum_of_nth_terms.py      12      0   100%
src/test_sum_positive.py           5      0   100%
------------------------------------------------------------
TOTAL                            408     15    96%

---------- coverage: platform darwin, python 3.5.2-final-0 -----------
Name                           Stmts   Miss  Cover   Missing
------------------------------------------------------------
src/alt_case.py                    2      0   100%
src/convert.py                     3      0   100%
src/disemvowel.py                  3      0   100%
src/even_odd.py                    4      0   100%
src/fatcat.py                      2      0   100%
src/get_grade.py                  11      0   100%
src/jenny.py                       4      0   100%
src/minmax.py                      8      0   100%
src/monkey.py                      2      0   100%
src/next_sq.py                     6      0   100%
src/parenthetics.py               45      3    93%   39, 68, 70
src/return_negative.py             2      0   100%
src/reverse.py                     2      0   100%
src/sort_bylength.py               2      0   100%
src/sort_cards.py                  7      0   100%
src/string2num.py                  2      0   100%
src/sum_highlow.py                 4      0   100%
src/sum_of_nth_terms.py            5      0   100%
src/sum_positive.py                4      0   100%
src/test_altcase.py               13      0   100%
src/test_convert.py                5      0   100%
src/test_disemvowel.py             6      0   100%
src/test_even_odd.py               5      0   100%
src/test_fatcat.py                13      0   100%
src/test_grade.py                 24      1    96%   48
src/test_jenny.py                  5      0   100%
src/test_minmax.py                22      0   100%
src/test_monkey.py                11      0   100%
src/test_nextsq.py                16      7    56%   26-27, 32-36
src/test_parenthetics.py          81      0   100%
src/test_return_negative.py       12      0   100%
src/test_reverse.py                6      0   100%
src/test_sort.py                  15      5    67%   28-32
src/test_sortlength.py            15      0   100%
src/test_string2num.py            10      0   100%
src/test_sum_highlow.py           14      0   100%
src/test_sum_of_nth_terms.py      12      0   100%
src/test_sum_positive.py           5      0   100%
------------------------------------------------------------
TOTAL                            408     16    96%


========================================================================= 171 passed in 6.06 seconds ==========================================================================
___________________________________________________________________________________ summary ___________________________________________________________________________________
  py27: commands succeeded
  py35: commands succeeded
  congratulations :)
```