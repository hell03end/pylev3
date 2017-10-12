import os
from .Levenshtein import Levenshtein


# for backward-compatibilty with original pylev
classic_levenshtein = Levenshtein.classic
recursive_levenshtein = Levenshtein.recursive
wf_levenshtein = Levenshtein.wf
wfi_levenshtein = Levenshtein.wfi
damerau_levenshtein = Levenshtein.damerau


# copy documentation from README
__doc__ = open(os.path.join(os.path.abspath("."), "README.md"), 'r').read()
__all__ = ("Levenshtein")  # import only Levenshtein class
__author__ = ("hell03end", "Daniel Lindsley")
__version__ = (1, 0, 0)
__license__ = "New BSD"  # as authored
