''' Main Levenshtein class (contain all functions as methods) '''

from functools import lru_cache

from .base import Singleton


class Levenshtein(Singleton):
    def __init__(self):
        super(Levenshtein, self).__init__()

    @staticmethod
    def _get_distance(obj_1: (str, list, tuple), obj_2: (str, list, tuple),
                      method: str) -> (int, list):
        '''
            Call correct class method to calculate Levenshtein distance

            >>> Levenshtein() is Levenshtein()
            True
            >>> Levenshtein._get_distance("abc", {"abc"}, "_classic")
            Traceback (most recent call last):
                ...
            ValueError: Parameters should be str or ordered collection
            >>> Levenshtein._get_distance("abc", {"abc"})
            Traceback (most recent call last):
                ...
            TypeError: _get_distance() missing 1 required positional argument: 'method'
        '''
        function = Levenshtein.__dict__[method].__func__
        if isinstance(obj_1, str) and isinstance(obj_2, str):
            return function(obj_1, obj_2)
        elif isinstance(obj_1, (list, tuple)) and \
                isinstance(obj_2, (list, tuple)):
            return [[function(s1, s2) for s2 in obj_2] for s1 in obj_1]
        elif isinstance(obj_1, str) and isinstance(obj_2, (list, tuple)):
            return [function(s, obj_1) for s in obj_2]
        elif isinstance(obj_2, str) and isinstance(obj_1, (list, tuple)):
            return [function(s, obj_2) for s in obj_1]
        else:
            raise ValueError("Parameters should be str or ordered collection")

    @staticmethod
    def _classic(string_1: str, string_2: str) -> int:
        if string_1 == string_2:
            return 0

        len_1 = len(string_1)
        len_2 = len(string_2)
        cost = 0

        if len_1 and len_2 and string_1[0] != string_2[0]:
            cost = 1

        if not len_1:
            return len_2
        elif not len_2:
            return len_1
        return min(
            Levenshtein._classic(string_1[1:], string_2) + 1,
            Levenshtein._classic(string_1, string_2[1:]) + 1,
            Levenshtein._classic(string_1[1:], string_2[1:]) + cost,
        )

    @staticmethod
    def classic(string_1: (str, (list, tuple)),
                string_2: (str, (list, tuple))) -> (int, list):
        """
            Calculates the Levenshtein distance between two strings.

            This version is easier to read, but significantly slower than the
            version below (up to several orders of magnitude). Useful for
            learning, less so otherwise.

            Usage::
                >>> Levenshtein.classic('kitten', 'sitting')
                3
                >>> Levenshtein.classic('kitten', 'kitten')
                0
                >>> Levenshtein.classic('', '')
                0
                >>> Levenshtein.classic('', 'abc')
                3
                >>> Levenshtein.classic(['abc', 'kit'], ['abs', 'kit'])
                [[1, 3], [3, 0]]
                >>> Levenshtein.classic(['abc', 'kit'], 'abc')
                [0, 3]
                >>> Levenshtein.classic('kit', ['abc', 'kit'])
                [3, 0]
        """
        return Levenshtein._get_distance(string_1, string_2, '_classic')

    @staticmethod
    def _recursive(string_1: str, string_2: str, len_1: int=None,
                   len_2: int=None, offset_1: int=0, offset_2: int=0,
                   memo: int=None) -> int:
        if string_1 == string_2:
            return 0

        if len_1 is None:
            len_1 = len(string_1)
        if len_2 is None:
            len_2 = len(string_2)
        if memo is None:
            memo = {}

        key = (offset_1, len_1, offset_2, len_2)
        cost = 0

        if memo.get(key, False):
            return memo[key]

        if not len_1:
            return len_2
        elif not len_2:
            return len_1

        if string_1[offset_1] != string_2[offset_2]:
            cost = 1

        dist = min(
            Levenshtein._recursive(string_1, string_2, len_1 - 1, len_2,
                                   offset_1 + 1, offset_2, memo) + 1,
            Levenshtein._recursive(string_1, string_2, len_1, len_2 - 1,
                                   offset_1, offset_2 + 1, memo) + 1,
            Levenshtein._recursive(string_1, string_2, len_1 - 1, len_2 - 1,
                                   offset_1 + 1, offset_2 + 1, memo) + cost
        )
        memo[key] = dist
        return dist

    @staticmethod
    def recursive(string_1: (str, (list, tuple)),
                  string_2: (str, (list, tuple))) -> (int, list):
        """
            Calculates the Levenshtein distance between two strings.

            Usage::
                >>> Levenshtein.recursive('kitten', 'sitting')
                3
                >>> Levenshtein.recursive('kitten', 'kitten')
                0
                >>> Levenshtein.recursive('', '')
                0
                >>> Levenshtein.recursive('', 'abc')
                3
                >>> Levenshtein.recursive(['abc', 'kit'], ['abs', 'kit'])
                [[1, 3], [3, 0]]
                >>> Levenshtein.recursive(['abc', 'kit'], 'abc')
                [0, 3]
                >>> Levenshtein.recursive('kit', ['abc', 'kit'])
                [3, 0]
        """
        return Levenshtein._get_distance(string_1, string_2, '_recursive')

    @staticmethod
    @lru_cache(maxsize=128)
    def _wf(string_1: str, string_2: str) -> int:
        if string_1 == string_2:
            return 0

        len_1 = len(string_1) + 1
        len_2 = len(string_2) + 1

        if not len_1 - 1:
            return len_2 - 1
        if not len_2 - 1:
            return len_1 - 1

        d = [0] * (len_1 * len_2)

        for i in range(len_1):
            d[i] = i
        for j in range(len_2):
            d[j * len_1] = j

        for j in range(1, len_2):
            for i in range(1, len_1):
                if string_1[i - 1] == string_2[j - 1]:
                    d[i + j * len_1] = d[i - 1 + (j - 1) * len_1]
                else:
                    d[i + j * len_1] = min(
                        d[i - 1 + j * len_1] + 1,        # deletion
                        d[i + (j - 1) * len_1] + 1,      # insertion
                        d[i - 1 + (j - 1) * len_1] + 1,  # substitution
                    )
        return d[-1]

    @staticmethod
    def wf(string_1: (str, (list, tuple)),
           string_2: (str, (list, tuple))) -> (int, list):
        """
            Calculates the Levenshtein distance between two strings.

            This version uses the Wagner-Fischer algorithm.

            Usage::
                >>> Levenshtein.wf('kitten', 'sitting')
                3
                >>> Levenshtein.wf('kitten', 'kitten')
                0
                >>> Levenshtein.wf('', '')
                0
                >>> Levenshtein.wf('', 'abc')
                3
                >>> Levenshtein.wf(['abc', 'kit'], ['abs', 'kit'])
                [[1, 3], [3, 0]]
                >>> Levenshtein.wf(['abc', 'kit'], 'abc')
                [0, 3]
                >>> Levenshtein.wf('kit', ['abc', 'kit'])
                [3, 0]
        """
        return Levenshtein._get_distance(string_1, string_2, '_wf')

    @staticmethod
    @lru_cache(maxsize=128)
    def _wfi(string_1: str, string_2: str) -> int:
        if string_1 == string_2:
            return 0

        len_1 = len(string_1)
        len_2 = len(string_2)

        if not len_1:
            return len_2
        if not len_2:
            return len_1

        if len_1 > len_2:
            string_2, string_1 = string_1, string_2
            len_2, len_1 = len_1, len_2

        d0 = [i for i in range(len_2 + 1)]
        d1 = [j for j in range(len_2 + 1)]

        for i in range(len_1):
            d1[0] = i + 1
            for j in range(len_2):
                cost = d0[j]
                if string_1[i] != string_2[j]:
                    # substitution
                    cost += 1
                    # insertion
                    x_cost = d1[j] + 1
                    if x_cost < cost:
                        cost = x_cost
                    # deletion
                    y_cost = d0[j + 1] + 1
                    if y_cost < cost:
                        cost = y_cost
                d1[j + 1] = cost
            d0, d1 = d1, d0
        return d0[-1]

    @staticmethod
    def wfi(string_1: (str, (list, tuple)),
            string_2: (str, (list, tuple))) -> (int, list):
        """
            Calculates the Levenshtein distance between two strings.

            This version uses an iterative version of the
            Wagner-Fischer algorithm.

            Usage::
                >>> Levenshtein.wfi('kitten', 'sitting')
                3
                >>> Levenshtein.wfi('kitten', 'kitten')
                0
                >>> Levenshtein.wfi('', '')
                0
                >>> Levenshtein.wfi('', 'abc')
                3
                >>> Levenshtein.wfi(['abc', 'kit'], ['abs', 'kit'])
                [[1, 3], [3, 0]]
                >>> Levenshtein.wfi(['abc', 'kit'], 'abc')
                [0, 3]
                >>> Levenshtein.wfi('kit', ['abc', 'kit'])
                [3, 0]
        """
        return Levenshtein._get_distance(string_1, string_2, '_wfi')

    @staticmethod
    @lru_cache(maxsize=128)
    def _damerau(string_1: str, string_2: str) -> int:
        if string_1 == string_2:
            return 0

        len_1 = len(string_1)
        len_2 = len(string_2)

        if len_1 == 0:
            return len_2
        if len_2 == 0:
            return len_1

        if len_1 > len_2:
            string_2, string_1 = string_1, string_2
            len_2, len_1 = len_1, len_2

        prev_cost = 0
        d0 = [i for i in range(len_2 + 1)]
        d1 = [j for j in range(len_2 + 1)]
        dprev = d0[:]

        s1 = string_1
        s2 = string_2

        for i in range(len_1):
            d1[0] = i + 1
            for j in range(len_2):
                cost = d0[j]
                if s1[i] != s2[j]:
                    # substitution
                    cost += 1
                    # insertion
                    x_cost = d1[j] + 1
                    if x_cost < cost:
                        cost = x_cost
                    # deletion
                    y_cost = d0[j + 1] + 1
                    if y_cost < cost:
                        cost = y_cost
                    # transposition
                    if i > 0 and j > 0 and s1[i] == s2[j - 1] \
                            and s1[i - 1] == s2[j]:
                        transp_cost = dprev[j - 1] + 1
                        if transp_cost < cost:
                            cost = transp_cost
                d1[j + 1] = cost
            dprev, d0, d1 = d0, d1, dprev
        return d0[-1]

    @staticmethod
    def damerau(string_1: (str, (list, tuple)),
                string_2: (str, (list, tuple))) -> (int, list):
        """
            Calculates the Damerau-Levenshtein distance between two strings.

            In addition to insertions, deletions and substitutions,
            Damerau-Levenshtein considers adjacent transpositions.

            This version is based on an iterative version of the
            Wagner-Fischer algorithm.

            Usage::
                >>> Levenshtein.damerau('kitten', 'sitting')
                3
                >>> Levenshtein.damerau('kitten', 'kittne')
                1
                >>> Levenshtein.damerau('', '')
                0
                >>> Levenshtein.damerau('', 'abc')
                3
                >>> Levenshtein.damerau(['abc', 'kit'], ['abs', 'kit'])
                [[1, 3], [3, 0]]
                >>> Levenshtein.damerau(['abc', 'kit'], 'abc')
                [0, 3]
                >>> Levenshtein.damerau('kit', ['abc', 'kit'])
                [3, 0]
        """
        return Levenshtein._get_distance(string_1, string_2, '_damerau')

    def __call__(self, string_1: (str, (list, tuple)),
                 string_2: (str, (list, tuple)), method: str="wfi") -> int:
        """
            Calculate Levenshtein distance with wfi method

            Usage::
                >>> Levenshtein()('kitten', 'sitting')
                3
                >>> Levenshtein()('kitten', 'kittne', method='wf')
                2
                >>> Levenshtein()('', '')
                0
                >>> Levenshtein()('', 'abc', 'damerau')
                3
                >>> Levenshtein()(['abc', 'kit'], ['abs', 'kit'])
                [[1, 3], [3, 0]]
                >>> Levenshtein()(['abc', 'kit'], 'abc')
                [0, 3]
                >>> Levenshtein()('kit', ['abc', 'kit'])
                [3, 0]
                >>> Levenshtein()('', '', method='sort')
                Traceback (most recent call last):
                    ...
                ValueError: Wrong method 'sort'
        """
        method = "_{}".format(method)
        if method not in self.__class__.__dict__:
            raise ValueError("Wrong method '{}'".format(method[1:]))
        return self._get_distance(string_1, string_2, method)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
