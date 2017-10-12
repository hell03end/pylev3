# pylev3
[![Build Status](https://travis-ci.org/hell03end/pylev.svg?branch=master)](https://travis-ci.org/hell03end/pylev)
[![PyPI version](https://badge.fury.io/py/pylev3.svg)](https://badge.fury.io/py/pylev3)

A Python3 Levenshtein distance (re)implementation of [pylev](https://github.com/toastdriven/pylev) (fork).

Calculation of Levenshtein distance between strings.
Based on the [Wikipedia code samples](http://en.wikipedia.org/wiki/Levenshtein_distance).

### Requirements
* Python Python 3.3+
* PyPy3

### Installation
```bash
    pip install pylev3
```

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

Or use old way (like in pylev):
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
New BSD (as authored, no changes :( ).

### Tests
```bash
    # get
    $ git clone https://github.com/hell03end/pylev.git
    $ cd pylev
    # run
    $ python -m unittest tests
```

### ToDo
* [ ] add extension for distance calculation on `c/c++` (preferably `c`)
* [ ] update tests & benchmarks
