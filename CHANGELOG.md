# Version History

## pylev3 changelog
* v1.0.1
    * add caching for non recursive Levenshtein implementations
    * add method selection for Levenshtein class call as function

* v1.0.0
    * renamed to pylev3
    * add hell03end to license
    * improve docs


## Changes for old versions
*Before pylev3*
* v1.3.3
    * Pass list of strings into any method to get result vector/matrix

* v1.3.2
    * Add \_\_call\_\_ into Levenshtein class
    * Divide main module into files

* v1.3.1
    * Reimplemented with Levenshtein class
    * Remove all Python versions except CPython3.3+

*Original pylev*
* v1.3.0
    * Implemented a considerably faster variants (orders of magnitude).
    * Tested & working on Python 2.7.4, Python 3.3.1 & PyPy 1.9.0.

* v1.2.0
    * Fixed all incorrect spellings of "Levenshtein" (there's no "c" in it).
    * Old methods are and use as usual (aliased for backward-compatibility.)

* v1.1.0
    * Implemented a much faster variant (several orders of magnitude).
    * The older variant was renamed to ``classic_levenschtein``.
    * Tested & working on Python 3.3 & PyPy 1.6.0 as well.

* v1.0.2
    * Python packaging is **REALLY** hard. Including the README *this time*.

* v1.0.1
    * Python packaging is hard. Including the README this time.

* v1.0.0
    * Initial release, just the naive implementation of Levenshtein.
