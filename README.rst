pylev3
======

.. image:: https://travis-ci.org/hell03end/pylev3.svg?branch=master
    :target: https://travis-ci.org/hell03end/pylev3
.. image:: https://badge.fury.io/py/pylev3.svg
    :target: https://badge.fury.io/py/pylev3

A Python3 Levenshtein distance (re)implementation of pylev_.

Calculation of Levenshtein distance between strings.
Based on the `Wikipedia code samples`_.

.. _pylev: https://github.com/toastdriven/pylev
.. _Wikipedia code samples: http://en.wikipedia.org/wiki/Levenshtein_distance

`What's new?`__

__ https://github.com/hell03end/pylev3/wiki/Changelog


Requirements
------------

* Python Python 3.3+ or PyPy3


Installation
------------

.. code-block:: bash

    pip install pylev3


Usage
-----

Usage is fairly straightforward:

.. code-block:: python

    from pylev3 import Levenshtein
    assert Levenshtein.classic('', 'cat'), 3
    assert Levenshtein.damerau('cat', 'cat'), 0
    assert Levenshtein.wf('kitten', 'sitting'), 3
    assert Levenshtein.wfi(['cat', 'kitten'], 'abc'), [3, 6]
    assert Levenshtein()(['cat', 'kitten'], ['cat', 'abc']), [[0, 3], [5, 6]]

Or use old way (like in pylev):

.. code-block:: python

    from pylev3 import wf_levenshtein, wfi_levenshtein, damerau_levenshtein, classic_levenshtein
    assert classic_levenshtein('', 'cat'), 3
    assert damerau_levenshtein('cat', 'cat'), 0
    assert wf_levenshtein('kitten', 'sitting'), 3
    assert wfi_levenshtein(['cat', 'kitten'], 'abc'), [3, 6]
    assert wf_levenshtein(['cat', 'kitten'], ['cat', 'abc']), [[0, 3], [5, 6]]


License
-------

New BSD (as authored).


Tests
-----

.. code-block:: bash

    # get
    $ git clone https://github.com/hell03end/pylev3.git
    $ cd pylev3
    # run
    $ python -m unittest tests
