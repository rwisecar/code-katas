"""Test for autocomplete module, taken from Code Wars website."""

import pytest
from autocomplete import Autocomplete


short_dictionary = ['fix', 'fax', 'fit', 'fist', 'full', 'finch', 'final', 'finial']

long_dictionary = ['airplane',  'apple', 'air', 'avenue', 'airport',
                     'adamantium', 'awkwardness', 'awesome', 'amazing',
                     'ball', 'book', 'bike', 'bill', 'billiard', 'bell',
                     'bowl', 'Blastoise', 'beautiful', 'car', 'cookie', 'coup',
                     'candle', 'change', 'champion', 'call', 'camel',
                     'charizard', 'catastrophic', 'cat', 'dog', 'down',
                     'dirigible', 'dare', 'doll', 'decode', 'digit',
                     'download', 'digital', 'dollar', 'decompose',
                     'declaration', 'dream', 'eat', 'excellent', 'elephant',
                     'ear', 'eye', 'eagle', 'evil', 'elevator', 'electronic',
                     'electron', 'elegant', 'easy', 'fairy', 'fin', 'flower',
                     'floral', 'float', 'fight', 'finish', 'finally', 'figure',
                     'gold', 'ghost', 'grate', 'grapes', 'giant', 'godzilla',
                     'gigantic', 'gigabyte', 'gremlin', 'gravel', 'game',
                     'gyarados', 'howl', 'house', 'hot', 'hidden', 'heat',
                     'hyrule', 'heart', 'health', 'hammer', 'harmony', 'igloo',
                     'inn', 'inside', 'inverted', 'infection', 'imagine',
                     'imagination', 'image', 'internal', 'impressive',
                     'inconceivable', 'jump', 'jumping', 'judge', 'judging',
                     'juggle', 'juggling', 'juggler', 'jiggle', 'jello',
                     'jelly', 'jam', 'king', 'key', 'kingdom', 'keepsake',
                     'kick', 'kicker', 'knot', 'kit', 'kitten', 'lamp',
                     'light', 'lol', 'llama', 'lake', 'love', 'link', 'league',
                     'legend', 'laboratory', 'lab', 'more', 'morbid', 'move',
                     'mover', 'movie', 'monocle', 'murica', 'molar', 'mouth',
                     'muscle', 'montage', 'nope', 'no', 'naughty', 'nice',
                     'nail polish', 'noodles', 'niece', 'nissan', 'octopus',
                     'orange', 'oval', 'orderly', 'order', 'orbit', 'ordinal',
                     'orion', 'pinch', 'pallet', 'paint', 'portrait',
                     'photograph', 'photo', 'pork', 'pig', 'pigeon', 'queen',
                     'quick', 'quickly', 'quest', 'question', 'quarry',
                     'quintuplets', 'query', 'quandary', 'quesadilla',
                     'royal', 'ruler', 'regal', 'rhino', 'rage', 'right',
                     'regular', 'regulate', 'regurgitate', 'reasonable',
                     'roll', 'rolling', 'same', 'sum', 'sip', 'sum', 'small',
                     'suggestion', 'seven', 'sink', 'sinker', 'string',
                     'tyrant', 'tiger', 'tired', 'tied', 'trick', 'trap',
                     'titan', 'titanic', 'tower', 'towering', 'trouble',
                     'terrific', 'terrible', 'this', 'umbrella', 'unicorn',
                     'under', 'undercover', 'united', 'unbelievable',
                     'unimaginable', 'ultra', 'ultraviolet', 'victory',
                     'violin', 'viola', 'vibrant', 'video playback', 'velcro',
                     'velvet', 'window', 'win', 'wedding', 'wet', 'where',
                     'wild', 'well', 'welcome', 'wonderful', 'xylophone',
                     'x-ray', 'x-Men', 'xavier', 'xenon', 'xerox', 'Xerneas',
                     'yaphi', 'you', 'yourself', 'your', 'yonder', 'yodel',
                     'yammer', 'yveltal', 'zelda', 'zygarde', 'zebra', 'zero',
                     'zeus', 'zap cannon', 'zephyr', 'zig-zag']


SHORT_DICT_PARAMS = [
    ['f', ['fix', 'fit', 'fist', 'finch', 'final']],
    ['fi', ['fix', 'fit', 'fist', 'finch', 'final']],
    ['fa', ['fax']],
    ['fu', ['full']],
    ['fin', ['finch', 'final', 'finial']],
    ['g', None],
    [' ', None]
]

SHORT_DICT_BIG_MAX_PARAMS = [
    ['f', ['fix', 'fit', 'fist', 'finch', 'final', 'finial', 'fax']],
    ['fi', ['fix', 'fit', 'fist', 'finch', 'final', 'finial']],
    ['fa', ['fax']],
    ['fu', ['full']],
    ['fin', ['finch', 'final', 'finial']],
    ['g', None],
    [' ', None]
]


LONG_DICT_PARAMS = [
    ['j', ['jump', 'jumping', 'judge', 'judging', 'juggle']],
    ['ji', ['jiggle']],
    ['i', ['igloo', 'inn', 'inside', 'inverted', 'infection']],
    ['in', ['inn', 'inside', 'inverted', 'infection', 'internal']],
    ['r', ['royal', 'roll', 'rolling', 'ruler', 'regal']],
    ['ro', ['royal', 'roll', 'rolling']],
    ['rol', ['roll', 'rolling']],
    ['x', ['xylophone', 'x-ray', 'x-men', 'xavier', 'xenon']],
    ['z', ['zelda', 'zebra', 'zero', 'zeus', 'zephyr']],
    ['q', ['queen', 'quest', 'question', 'quesadilla', 'query']],
    ['que', ['queen', 'quest', 'question', 'quesadilla', 'query']],
    ['qui', ['quick', 'quickly', 'quintuplets']],
    ['b', ['ball', 'book', 'bowl', 'bike', 'bill']],
    ['bi', ['bike', 'bill', 'billiard']],
    ['bil', ['bill', 'billiard']]
]


LONG_DICT_BIG_MAX_PARAMS = [
    ['j', ['jump', 'jumping', 'judge', 'judging', 'juggle', 'juggler',
     'juggling']],
    ['ji', ['jiggle']],
    ['i', ['igloo', 'inn', 'inside', 'inverted', 'infection', 'internal',
     'inconceivable']],
    ['in', ['inn', 'inside', 'inverted', 'infection', 'internal',
     'inconceivable']],
    ['r', ['royal', 'roll', 'rolling', 'ruler', 'regal', 'regular',
     'regulate']],
    ['ro', ['royal', 'roll', 'rolling']],
    ['rol', ['roll', 'rolling']],
    ['x', ['xylophone', 'x-ray', 'x-men', 'xavier', 'xenon', 'xerox',
     'xerneas']],
    ['z', ['zelda', 'zebra', 'zero', 'zeus', 'zephyr', 'zygarde',
     'zap cannon']],
    ['q', ['queen', 'quest', 'question', 'quesadilla', 'query', 'quick',
     'quickly']],
    ['que', ['queen', 'quest', 'question', 'quesadilla', 'query']],
    ['qui', ['quick', 'quickly', 'quintuplets']],
    ['b', ['ball', 'book', 'bowl', 'bike', 'bill', 'billiard', 'bell']],
    ['bi', ['bike', 'bill', 'billiard']],
    ['bil', ['bill', 'billiard']]
]

LONG_DICT_VERY_BIG_PARAMS = [
    ['a', ['airplane', 'airport', 'air', 'apple', 'avenue', 'adamantium',
     'awkwardness', 'awesome', 'amazing']],
    ['e', ['eat', 'ear', 'eagle', 'easy', 'excellent', 'elephant', 'elevator',
     'electronic', 'electron', 'elegant', 'eye', 'evil']],
    ['p', ['pinch', 'pig', 'pigeon', 'pallet', 'paint', 'portrait', 'pork',
     'photograph', 'photo']],
]

# ----------------------------------FIXTURES-----------------------------------


@pytest.fixture
def short_dict_trie():
    """A trie filled with words from the short dictionary."""
    return Autocomplete(short_dictionary)


@pytest.fixture
def short_dict_big_max():
    """A trie filled with words from the short dictionary, max_compl = 7."""
    return Autocomplete(short_dictionary, max_completions=7)


@pytest.fixture
def long_dict_trie():
    """A trie filled with words from the short dictionary."""
    return Autocomplete(long_dictionary)


@pytest.fixture
def long_dict_big_max():
    """A trie filled with words from the short dictionary, max_compl = 7."""
    return Autocomplete(long_dictionary, max_completions=7)


@pytest.fixture
def long_dict_very_big_max():
    """A trie filled with words from the short dictionary, max_compl = 7."""
    return Autocomplete(long_dictionary, max_completions=15)


# -----------------------------SHORT DICTIONARY TESTS--------------------------


@pytest.mark.parametrize("n, result", SHORT_DICT_PARAMS)
def test_basic_use_cases_short_dictionary(n, result, short_dict_trie):
    """Test the basic use cases for the short dictionary."""
    assert short_dict_trie.autocomplete(n) == result


@pytest.mark.parametrize("n, result", SHORT_DICT_BIG_MAX_PARAMS)
def test_basic_use_cases_short_dict_big_max(n, result, short_dict_big_max):
    """Test basic use cases for short dictionary with long max_completions."""
    assert short_dict_big_max.autocomplete(n) == result


def test_error_if_not_string():
    """Test that you get a TypeError if you try to input a nonstring."""
    with pytest.raises(TypeError):
        Breakit = Autocomplete([1, 2, 3])


# ------------------------------LONG DICTIONARY TESTS--------------------------


@pytest.mark.parametrize("n, result", LONG_DICT_PARAMS)
def test_basic_use_cases_long_dictionary(n, result, long_dict_trie):
    """Test the basic use cases for the long dictionary."""
    assert long_dict_trie.autocomplete(n) == result


@pytest.mark.parametrize("n, result", LONG_DICT_BIG_MAX_PARAMS)
def test_basic_use_cases_long_dict_big_max(n, result, long_dict_big_max):
    """Test basic use cases for long dictionary with longer max_completions."""
    assert long_dict_big_max.autocomplete(n) == result


@pytest.mark.parametrize("n, result", LONG_DICT_VERY_BIG_PARAMS)
def test_very_long_max_completions(n, result, long_dict_very_big_max):
    """Test basic use cases for long dictionary w longest max_completions."""
    assert long_dict_very_big_max.autocomplete(n) == result
