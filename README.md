# pylev (fork)
[![Build Status](https://travis-ci.org/hell03end/pylev.svg?branch=master)](https://travis-ci.org/hell03end/pylev)

A pure Python Levenshtein implementation that's not freaking GPL'd.

Based off the [Wikipedia code samples](http://en.wikipedia.org/wiki/Levenshtein_distance).

**[Original version](https://github.com/toastdriven/pylev)**.


### Requirements
* Python Python 3.3+
* PyPy3


### Usage
Usage is fairly straightforward:

```python
    from pylev import Levenshtein

    assert Levenshtein.classic('', 'cat'), 3
    assert Levenshtein.damerau('cat', 'cat'), 0
    assert Levenshtein.wf('kitten', 'sitting'), 3
    assert Levenshtein.wfi(['cat', 'kitten'], 'abc'), [3, 6]
    assert Levenshtein()(['cat', 'kitten'], ['cat', 'abc']), [[0, 3], [5, 6]]
```

Or use old way:
```python
    from pylev import (
        wf_levenshtein, wfi_levenshtein, damerau_levenshtein,
        classic_levenshtein
    )

    assert classic_levenshtein('', 'cat'), 3
    assert damerau_levenshtein('cat', 'cat'), 0
    assert wf_levenshtein('kitten', 'sitting'), 3
    assert wfi_levenshtein(['cat', 'kitten'], 'abc'), [3, 6]
    assert wf_levenshtein(['cat', 'kitten'], ['cat', 'abc']), [[0, 3], [5, 6]]
```


### License
New BSD (as authored, no changes).


### Tests
```bash
    # get
    $ git clone https://github.com/hell03end/pylev.git
    $ cd pylev
    # run
    $ python -m unittest tests
```


### Changelog
* v1.3.3
    * Pass list of strings into any method to get result vector/matrix

* v1.3.2
    * Add \_\_call\_\_ into Levenshtein class
    * Divide main module into files

* v1.3.1
    * Reimplemented with Levenshtein class
    * Remove all Python versions except CPython3.3+

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
