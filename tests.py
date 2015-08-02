import itertools
import unittest
import pylev

from fixtures.corpus import iter_solutions


class Tests(unittest.TestCase):

    def test_damerau_levenshtein(self):
        assert pylev.damerau_levenshtein("ba", "abc") == 2
        assert pylev.damerau_levenshtein("foobar", "foobra") == 1
        assert pylev.damerau_levenshtein("fee", "deed") == 2

    def test_levenshtein_words_corpus(self):
        for a, b, distance in iter_solutions('word_lev_distances'):
            assert pylev.levenshtein(a, b) == distance

    def test_damerau_words_corpus(self):
        for a, b, distance in iter_solutions('word_dam_distances'):
            assert pylev.damerau_levenshtein(a, b) == distance

    def test_levenshtein_sentances_corpus(self):
        for a, b, distance in iter_solutions('sentance_lev_distances'):
            assert pylev.levenshtein(a, b) == distance

    def test_damerau_sentances_corpus(self):
        for a, b, distance in iter_solutions('sentance_dam_distances'):
            assert pylev.damerau_levenshtein(a, b) == distance


def _mk_test_fn(fn, a, b, expected):
    def _test_fn(self):
        self.assertEqual(fn(a, b), expected)
        self.assertEqual(fn(b, a), expected)

    return _test_fn


test_data = [
    ('classic', "kitten", "sitting", 3),
    ('same', "kitten", "kitten", 0),
    ('empty', "", "", 0),
    ('a', "meilenstein", "levenshtein", 4),
    ('b', "levenshtein", "frankenstein", 6),
    ('c', "confide", "deceit", 6),
    ('d', "CUNsperrICY", "conspiracy", 8),
]

test_functions = [
    # pylev.classic_levenshtein,   # disabled because it is so slow
    pylev.recursive_levenshtein,
    pylev.wf_levenshtein,
    pylev.wfi_levenshtein,
    pylev.expanded_wfi_levenshtein
]


for lev_fn, data in itertools.product(test_functions, test_data):
    name, a, b, expected = data
    test_fn = _mk_test_fn(lev_fn, a, b, expected)
    setattr(Tests, "test_{}_{}".format(name, lev_fn.__name__), test_fn)


if __name__ == '__main__':
    unittest.main()
