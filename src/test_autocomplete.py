"""Test for autocomplete module, taken from Code Wars website."""

import pytest
from autocomplete import autocomplete


def solution(input_, dictionary):
    """Solution taken from code wars for testing purposes."""
    return lambda input_, dictionary: [
        item for item in dictionary if item.lower().startswith(
            "".join([l for l in input_ if l.isalpha()]).lower())][:5]


dictionaryNoGuess = ['airplane',  'apple', 'air', 'avenue', 'airport',
                     'adamantium', 'awkwardness', 'awesome', 'amazing',
                     'ball', 'book', 'bike', 'bill', 'billiard', 'bell',
                     'bowl', 'Blastoise', 'beautiful', 'car', 'cookie', 'coup',
                     'candle', 'change', 'champion', 'call', 'camel',
                     'Charizard', 'catastrophic', 'cat', 'dog', 'down',
                     'dirigible', 'dare', 'doll', 'decode', 'digit',
                     'download', 'digital', 'dollar', 'decompose',
                     'declaration', 'dream', 'eat', 'excellent', 'elephant',
                     'ear', 'eye', 'eagle', 'evil', 'elevator', 'electronic',
                     'electron', 'elegant', 'easy', 'fairy', 'fin', 'flower',
                     'floral', 'float', 'fight', 'finish', 'finally', 'figure',
                     'gold', 'ghost', 'grate', 'grapes', 'giant', 'godzilla',
                     'gigantic', 'gigabyte', 'gremlin', 'gravel', 'game',
                     'Gyarados', 'howl', 'house', 'hot', 'hidden', 'heat',
                     'Hyrule', 'heart', 'health', 'hammer', 'harmony', 'igloo',
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
                     'x-ray', 'X-Men', 'Xavier', 'xenon', 'xerox', 'Xerneas',
                     'Yaphi', 'you', 'yourself', 'your', 'yonder', 'yodel',
                     'yammer', 'Yveltal', 'Zelda', 'Zygarde', 'zebra', 'zero',
                     'Zeus', 'zap cannon', 'zephyr', 'zig-zag']


BASIC_TEST_PARAMS = [
        ['ai', ['airplane', 'air', 'airport']],
        ['z', ['Zelda', 'Zygarde', 'zebra', 'zero', 'Zeus']],
        ['t', ['tyrant', 'tiger', 'tired', 'tied', 'trick']],
        ['nothinghere', []],
        ['yaph', ['Yaphi']],
        ['nope', ['nope']],
        ['n~!@#$%^&*()_+1234567890ope', ['nope']],
        ['""', ['airplane', 'apple', 'air', 'avenue', 'airport']]
]


@pytest.mark.parametrize("input, result", BASIC_TEST_PARAMS)
def test_ai(input, result):
    """Test that input_ 'ai' returns correct words."""
    assert autocomplete(input, dictionaryNoGuess) == result


def random_tests():
    """Test that input_ with random values returns correct sets."""
    from random import randint
    prev = ['','^','$','_',' ','-','#','','','','','','','','','','','','']
    base = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    foll = ['','i','','a','','o','','u','','e','$','^','*','#','@','','','','','','','','','','','','','']

    for _ in xrange(40):
        i = "".join([prev[randint(0,len(prev)-1)]]+[base[randint(0,len(base)-1)]]+[foll[randint(0,len(foll)-1)]])
        assert autocomplete(i, dictionaryNoGuess) == solution(i, dictionaryNoGuess)