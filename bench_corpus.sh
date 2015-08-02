#!/bin/bash
echo -ne "pypy exp_wfi_levenshtein\t\t\t"
pypy -m timeit -s "import pylev;import fixtures.corpus as c" "for a, b, d in c.iter_solutions('word_lev_distances'): assert d == pylev.expanded_wfi_levenshtein(a, b)"
echo -ne "pypy std_wfi_levenshtein\t\t\t"
pypy -m timeit -s "import pylev;import fixtures.corpus as c" "for a, b, d in c.iter_solutions('word_lev_distances'): assert d == pylev.wfi_levenshtein(a, b)"
#echo -ne "py2 wfi_levenshtein\t\t\t"
#python2 -m timeit -s "import pylev;import fixtures.corpus as c" "for a, b, d in c.iter_solutions('word_lev_distances'): pylev.wfi_levenshtein(a, b)"
#echo -ne "py3 wfi_levenshtein\t\t\t"
#python3 -m timeit -s "import pylev;import fixtures.corpus as c" "for a, b, d in c.iter_solutions('word_lev_distances'): pylev.wfi_levenshtein(a, b)"
