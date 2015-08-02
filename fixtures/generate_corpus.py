import gzip
import random
import itertools

from corpus import read_words, read_sentances, PATHS

# pip install python-levenshtein
# sudo apt-get install python3-dev
import Levenshtein
# pip install editdistance
import editdistance
# pip install numpy
# pip install pyxDamerauLevenshtein
import pyxdameraulevenshtein
import pylev


def write_combo_distances(elements):
    for a, b in itertools.product(elements, elements):
        dist1 = editdistance.eval(a, b)
        dist2 = Levenshtein.distance(a, b)
        dist3 = pyxdameraulevenshtein.damerau_levenshtein_distance(a, b)
        dist4 = pylev.levenshtein(a, b)
        assert dist1 == dist2
        assert dist2 == dist4
        assert dist1 < 256
        assert dist3 < 256
        levenshtein_fh.write(bytes((dist1,)))
        damerau_fh.write(bytes((dist3,)))


def iter_sentances():
    words = read_words()
    rand = random.Random(1)

    return (
        [" ".join(rand.sample(words, 8)) for i in range(10)] +
        [" ".join(rand.sample(words, 16)) for i in range(10)]
    )


with open(PATHS['sentances'], mode='w', encoding='utf-8') as fh:
    for sentance in iter_sentances():
        fh.write(sentance + "\n")

levenshtein_fh = gzip.open(PATHS['word_lev_distances'], mode='wb')
damerau_fh = gzip.open(PATHS['word_dam_distances'], mode='wb')

write_combo_distances(read_words())

levenshtein_fh = gzip.open(PATHS['sentance_lev_distances'], mode='wb')
damerau_fh = gzip.open(PATHS['sentance_dam_distances'], mode='wb')

write_combo_distances(read_sentances())
