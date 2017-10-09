"""
    pylev (fork by hell03end)
    =====

    A Python Levenshtein OOP implementation that's not freaking GPL'd.

    Based off the Wikipedia code samples at
    http://en.wikipedia.org/wiki/Levenshtein_distance.
    Original version: https://github.com/toastdriven/pylev.

    Usage
    -----

    Usage is fairly straightforward:

        from pylev import Levenshtein
        >>> Levenshtein().wf('kitten', 'sitting')
        3
"""

from .Levenshtein import Levenshtein


# for backward-compatibilty with original pylev
classic_levenshtein = Levenshtein.classic
recursive_levenshtein = Levenshtein.recursive
wf_levenshtein = Levenshtein.wf
wfi_levenshtein = Levenshtein.wfi
damerau_levenshtein = Levenshtein.damerau


# import only Levenshtein class
__all__ = ("Levenshtein")
__author__ = ('Daniel Lindsley', 'hell03end')
__version__ = (1, 3, 3)
__license__ = 'New BSD'  # as authored
