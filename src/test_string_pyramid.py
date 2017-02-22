"""Tests for the string pyramid module, taken from Code Wars."""

from random import choice, randint
from string import ascii_letters, digits, punctuation

VALID_CHARS = '{}{}{}'.format(ascii_letters, digits, punctuation)


def my_watch_pyramid_from_the_side(characters):
    width = 2 * len(characters) - 1
    output = '{{:^{}}}'.format(width).format
    return '\n'.join(output(char * dex) for char, dex in
                     zip(reversed(characters), range(1, width + 1, 2)))


def my_watch_pyramid_from_above(characters):
    width = 2 * len(characters) - 1
    dex = width - 1
    result = []
    for a in range(width):
        row = []
        for b in range(width):
            minimum, maximum = sorted((a, b))
            row.append(characters[min(abs(dex - maximum), abs(0 - minimum))])
        result.append(''.join(row))
    return '\n'.join(result)


def my_count_visible_characters_of_the_pyramid(characters):
    return (2 * len(characters) - 1) ** 2


def my_count_all_characters_of_the_pyramid(characters):
    return sum(a ** 2 for a in range(1, 2 * len(characters), 2))


def random_string():
    return ''.join(choice(VALID_CHARS) for _ in range(randint(1, 10)))


def visualisation(expected_watch_from_side, expected_watch_from_above,
                  actual_watch_from_side, actual_watch_from_above):
    print('From side correct:\n{}'.format(expected_watch_from_side))
    print('--------------------------------------')
    print('From above correct:\n{}'.format(expected_watch_from_above))
    print('--------------------------------------')
    print('From side yours:\n{}'.format(actual_watch_from_side))
    print('--------------------------------------')
    print('From above yours:\n{}'.format(actual_watch_from_above))
    Test.assert_equals(actual_watch_from_side, expected_watch_from_side)
    Test.assert_equals(actual_watch_from_above, expected_watch_from_above)


# None or Empty
Test.describe('None or Empty Tests')
Test.it('should handle None and empty')
Test.assert_equals(watch_pyramid_from_the_side(None), None)
Test.assert_equals(watch_pyramid_from_above(None), None)
Test.assert_equals(count_visible_characters_of_the_pyramid(None), -1)
Test.assert_equals(count_all_characters_of_the_pyramid(None), -1)
Test.assert_equals(watch_pyramid_from_the_side(''), '')
Test.assert_equals(watch_pyramid_from_above(''), '')
Test.assert_equals(count_visible_characters_of_the_pyramid(''), -1)
Test.assert_equals(count_all_characters_of_the_pyramid(''), -1)

# Basic Tests
Test.describe('Basic Tests')
Test.it('should handle 2 characters')
characters = '*#'
expected_watch_from_side = '''\
 # 
***'''
expected_watch_from_above = '''\
***
*#*
***'''
actual_watch_from_side = watch_pyramid_from_the_side(characters)
actual_watch_from_above = watch_pyramid_from_above(characters)
visualisation(
    expected_watch_from_side, expected_watch_from_above,
    actual_watch_from_side, actual_watch_from_above
)
Test.assert_equals(count_visible_characters_of_the_pyramid(characters), 9)
Test.assert_equals(count_all_characters_of_the_pyramid(characters), 10)

Test.it('should handle 3 characters')
characters = 'abc'
expected_watch_from_side = '''\
  c  
 bbb 
aaaaa'''
expected_watch_from_above = '''\
aaaaa
abbba
abcba
abbba
aaaaa'''
actual_watch_from_side = watch_pyramid_from_the_side(characters)
actual_watch_from_above = watch_pyramid_from_above(characters)
visualisation(
    expected_watch_from_side, expected_watch_from_above,
    actual_watch_from_side, actual_watch_from_above
)
Test.assert_equals(count_visible_characters_of_the_pyramid(characters), 25)
Test.assert_equals(count_all_characters_of_the_pyramid(characters), 35)

Test.it('should handle 3 same characters')
characters = 'aaa'
expected_watch_from_side = '''\
  a  
 aaa 
aaaaa'''
expected_watch_from_above = '''\
aaaaa
aaaaa
aaaaa
aaaaa
aaaaa'''
actual_watch_from_side = watch_pyramid_from_the_side(characters)
actual_watch_from_above = watch_pyramid_from_above(characters)
visualisation(expected_watch_from_side, expected_watch_from_above,
              actual_watch_from_side, actual_watch_from_above)
Test.assert_equals(count_visible_characters_of_the_pyramid(characters), 25)
Test.assert_equals(count_all_characters_of_the_pyramid(characters), 35)

Test.it('should handle 5 descending ordered characters')
characters = '54321'
expected_watch_from_side = '''\
    1    
   222   
  33333  
 4444444 
555555555'''

expected_watch_from_above = '''\
555555555
544444445
543333345
543222345
543212345
543222345
543333345
544444445
555555555'''
actual_watch_from_side = watch_pyramid_from_the_side(characters)
actual_watch_from_above = watch_pyramid_from_above(characters)
visualisation(expected_watch_from_side, expected_watch_from_above,
              actual_watch_from_side, actual_watch_from_above)
Test.assert_equals(count_visible_characters_of_the_pyramid(characters), 81)
Test.assert_equals(count_all_characters_of_the_pyramid(characters), 165)

# Random
Test.describe('Random Tests')
Test.it('should handle random characters')

for _ in range(100):
    characters = random_string()
    Test.assert_equals(watch_pyramid_from_the_side(characters),
                       my_watch_pyramid_from_the_side(characters))
    Test.assert_equals(watch_pyramid_from_above(characters),
                       my_watch_pyramid_from_above(characters))
    Test.assert_equals(count_visible_characters_of_the_pyramid(characters),
                       my_count_visible_characters_of_the_pyramid(characters))
    Test.assert_equals(count_all_characters_of_the_pyramid(characters),
                       my_count_all_characters_of_the_pyramid(characters))