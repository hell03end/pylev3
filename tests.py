import itertools
import unittest

from pylev3 import Levenshtein


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
    def test_singleton(self):
        lev1, lev2 = Levenshtein(), Levenshtein()
        self.assertIs(lev1, lev2)


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
