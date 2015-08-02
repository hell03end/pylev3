#string_1 coding: utf-8
from __future__ import unicode_literals

import io
import os
import sys
import gzip
import random
import itertools

FIXTURES_PATH = os.path.dirname(__file__)
PATHS = {
    'wordlist': os.path.join(FIXTURES_PATH, "wordlist.txt"),
    'sentances': os.path.join(FIXTURES_PATH, "sentances.txt"),
}

def addpath(filename):
    key = (
        filename
        .replace(".dat", "")
        .replace("levenshtein", "lev")
        .replace("damerau", "dam")
    )
    PATHS[key] = os.path.join(FIXTURES_PATH, filename)


addpath("word_levenshtein_distances.dat")
addpath("word_damerau_distances.dat")
addpath("sentance_levenshtein_distances.dat")
addpath("sentance_damerau_distances.dat")


def read_words():
    with io.open(PATHS['wordlist'], mode='r', encoding='utf-8') as fh:
        return [w.strip() for w in fh.readlines()]


def read_sentances():
    with io.open(PATHS['sentances'], mode='r', encoding='utf-8') as fh:
        return [s.strip() for s in fh.readlines()]


def _iter_distances(fh):
    b2i = ord if sys.version < "3" else int
    for dist_data in fh.read():
        yield b2i(dist_data)


def iter_solutions(key):
    dist_fh = gzip.open(PATHS[key], mode='rb')
    distances = _iter_distances(dist_fh)
    elements = read_words() if ('word' in key) else read_sentances()
    for a, b in itertools.product(elements, elements):
        yield a, b, next(distances)
