from __future__ import annotations
from group import Group, Word


def generate_sym_group(n: int):
    class SymmetricGroup(Group):
        """
        Group operations for Symmetric groups of size n

        Group elements are expected to be lists of length n containing
        the integers from 0 to n-1 corresponding to permutations in two
        row notation with the index representing the first row and list
        elements the second row.
        """

        element_t = list[int]
        size = n
        name = "S_" + str(n)

        # Identity is the empty permutation
        Id = list(range(n))

        @classmethod
        def compute_word(cls, word: Word):
            """Compute canonical form of word (array-like) elements by applying the group operation in sequence"""
            if len(word) == 0:
                # Empty word equals the identity by convention
                return cls.Id
            elif len(word) == 1:
                if word.indices[0]:
                    return cls.inverse(word.elements[0])
                else:
                    return word.elements[0]
            else:
                norm_form = cls.Id
                for i in range(len(word)):
                    norm_form = cls.operation(
                        norm_form, word.elements[i], b_ind=word.indices[i]
                    )
            return norm_form

        @classmethod
        def inverse(cls, a: element_t) -> element_t:
            """ Compute the inverse of a permutation by inverting each cycle"""
            assert sorted(a) == cls.Id
            return [a.index(i) for i in range(cls.size)]

        @classmethod
        def operation(
            cls, a: element_t, b: element_t, a_ind: bool = False, b_ind: bool = False
        ) -> list[int]:
            """Compose two permutations"""
            assert (sorted(a) == cls.Id) and (sorted(b) == cls.Id)
            if not a_ind:
                a = cls.inverse(a)
            if not b_ind:
                b = cls.inverse(b)
            return [a.index(b.index(i)) for i in range(cls.size)]

        @classmethod
        def canonize(cls, word: Word) -> element_t:
            """Put word into canonical form
            in this case the product of its symbols in S_n
            presented in the two line form"""
            return cls.compute_word(word)

    return SymmetricGroup
