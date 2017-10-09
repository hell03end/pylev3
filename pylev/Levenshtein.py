''' Main Levenshtein class (contain all functions as methods) '''


class Levenshtein(object):
    def __init__(self):
        super(Levenshtein, self).__init__()

    @staticmethod
    def classic(string_1: str, string_2: str) -> int:
        """
            Calculates the Levenshtein distance between two strings.

            This version is easier to read, but significantly slower than the
            version below (up to several orders of magnitude). Useful for
            learning, less so otherwise.

            Usage::
                >>> Levenshtein().classic('kitten', 'sitting')
                3
                >>> Levenshtein().classic('kitten', 'kitten')
                0
                >>> Levenshtein().classic('', '')
                0
                >>> Levenshtein().classic('', 'abc')
                3
        """
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
            Levenshtein.classic(string_1[1:], string_2) + 1,
            Levenshtein.classic(string_1, string_2[1:]) + 1,
            Levenshtein.classic(string_1[1:], string_2[1:]) + cost,
        )

    @staticmethod
    def recursive(string_1: str, string_2: str, len_1: int=None,
                  len_2: int=None, offset_1: int=0, offset_2: int=0,
                  memo: int=None) -> int:
        """
            Calculates the Levenshtein distance between two strings.

            Usage::
                >>> Levenshtein().recursive('kitten', 'sitting')
                3
                >>> Levenshtein().recursive('kitten', 'kitten')
                0
                >>> Levenshtein().recursive('', '')
                0
                >>> Levenshtein().recursive('', 'abc')
                3
        """
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
            Levenshtein.recursive(string_1, string_2, len_1 - 1, len_2,
                                  offset_1 + 1, offset_2, memo) + 1,
            Levenshtein.recursive(string_1, string_2, len_1, len_2 - 1,
                                  offset_1, offset_2 + 1, memo) + 1,
            Levenshtein.recursive(string_1, string_2, len_1 - 1, len_2 - 1,
                                  offset_1 + 1, offset_2 + 1, memo) + cost
        )
        memo[key] = dist
        return dist

    @staticmethod
    def wf(string_1: str, string_2: str) -> int:
        """
            Calculates the Levenshtein distance between two strings.

            This version uses the Wagner-Fischer algorithm.

            Usage::
                >>> Levenshtein().wf('kitten', 'sitting')
                3
                >>> Levenshtein().wf('kitten', 'kitten')
                0
                >>> Levenshtein().wf('', '')
                0
                >>> Levenshtein().wf('', 'abc')
                3
        """

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
    def wfi(string_1: str, string_2: str) -> int:
        """
            Calculates the Levenshtein distance between two strings.

            This version uses an iterative version of the
            Wagner-Fischer algorithm.

            Usage::
                >>> Levenshtein().wfi('kitten', 'sitting')
                3
                >>> Levenshtein().wfi('kitten', 'kitten')
                0
                >>> Levenshtein().wfi('', '')
                0
                >>> Levenshtein().wfi('', 'abc')
                3
        """
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
    def damerau(string_1: str, string_2: str) -> int:
        """
            Calculates the Damerau-Levenshtein distance between two strings.

            In addition to insertions, deletions and substitutions,
            Damerau-Levenshtein considers adjacent transpositions.

            This version is based on an iterative version of the
            Wagner-Fischer algorithm.

            Usage::
                >>> Levenshtein().damerau('kitten', 'sitting')
                3
                >>> Levenshtein().damerau('kitten', 'kittne')
                1
                >>> Levenshtein().damerau('', '')
                0
                >>> Levenshtein().damerau('', 'abc')
                3
        """
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

    def __call__(self, string_1: str, string_2: str) -> int:
        """
            Usage::
                >>> Levenshtein()('kitten', 'sitting')
                3
                >>> Levenshtein()('kitten', 'kittne')
                2
                >>> Levenshtein()('', '')
                0
                >>> Levenshtein()('', 'abc')
                3
        """
        return self.wfi(string_1, string_2)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
