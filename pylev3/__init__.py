'''
    pylev3
    ======

    A Python3 Levenshtein distance (re)implementation of pylev.
    Calculation of Levenshtein distance between strings.

    Usage
    -----

    from pylev import Levenshtein
    assert Levenshtein.classic('', 'cat'), 3
    assert Levenshtein.damerau('cat', 'cat'), 0
    assert Levenshtein.wf('kitten', 'sitting'), 3
    assert Levenshtein.wfi(['cat', 'kitten'], 'abc'), [3, 6]
    assert Levenshtein()(['cat', 'car'], ['cat', 'abc']), [[0, 3], [1, 3]]
'''

import os
from .Levenshtein import Levenshtein


# for backward-compatibilty with original pylev
classic_levenshtein = Levenshtein.classic
recursive_levenshtein = Levenshtein.recursive
wf_levenshtein = Levenshtein.wf
wfi_levenshtein = Levenshtein.wfi
damerau_levenshtein = Levenshtein.damerau


__all__ = ("Levenshtein")  # import only Levenshtein class
__author__ = ("hell03end", "Daniel Lindsley")
__version__ = (1, 1, 0)
__license__ = "New BSD"  # as authored
