import itertools
import unittest

from pylev3 import Levenshtein
from fixtures.corpus import iter_solutions

TEST_DATA = [
    ('classic', "kitten", "sitting", 3),
    ('same', "kitten", "kitten", 0),
    ('empty', "", "", 0),
    ('a', "meilenstein", "levenshtein", 4),
    ('b', "levenshtein", "frankenstein", 6),
    ('c', "confide", "deceit", 6),
    ('d', "CUNsperrICY", "conspiracy", 8),
]

TEST_FUNCTIONS = [
    # Levenshtein().classic,  # too slow
    Levenshtein().recursive,
    Levenshtein().wf,
    Levenshtein().wfi,
    Levenshtein().damerau
]


class Tests(unittest.TestCase):
    def test_damerau_levenshtein(self):
        assert Levenshtein().damerau("ba", "abc") == 2
        assert Levenshtein().damerau("foobar", "foobra") == 1
        assert Levenshtein().damerau("fee", "deed") == 2

    def test_levenshtein_words_corpus(self):
        for a, b, distance in iter_solutions('word_lev_distances'):
            assert Levenshtein()(a, b) == distance

    def test_damerau_words_corpus(self):
        for a, b, distance in iter_solutions('word_dam_distances'):
            assert Levenshtein().damerau(a, b) == distance

    def test_levenshtein_sentances_corpus(self):
        for a, b, distance in iter_solutions('sentance_lev_distances'):
            assert Levenshtein()(a, b) == distance

    def test_damerau_sentances_corpus(self):
        for a, b, distance in iter_solutions('sentance_dam_distances'):
            assert Levenshtein().damerau(a, b) == distance


def _mk_test_fn(fn, a, b, expected):
    def _test_fn(self):
        self.assertEqual(fn(a, b), expected)
        self.assertEqual(fn(b, a), expected)
    return _test_fn


for lev_fn, data in itertools.product(TEST_FUNCTIONS, TEST_DATA):
    name, a, b, expected = data
    test_fn = _mk_test_fn(lev_fn, a, b, expected)
    setattr(Tests, "test_{}_{}".format(name, lev_fn.__name__), test_fn)


if __name__ == '__main__':
    unittest.main()
