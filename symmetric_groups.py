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


if __name__ == "__main__":
    # Unit tests
    # TODO: Move this into pytest
    print("Running unit tests")
    print("Testing initialisation, group operation, inverses")

    Sym_3 = generate_sym_group(3)
    assert Sym_3.size == 3
    assert Sym_3.name == "S_3"
    assert Sym_3.Id == list(range(3))
    assert Sym_3.inverse(Sym_3.Id) == Sym_3.Id
    assert Sym_3.operation(Sym_3.Id, Sym_3.Id) == Sym_3.Id
    assert Sym_3.operation(Sym_3.Id, [2, 1, 0]) == [2, 1, 0]
    assert Sym_3.operation([2, 1, 0], Sym_3.Id) == [2, 1, 0]

    Sym_4 = generate_sym_group(4)
    assert Sym_4.size == 4
    assert Sym_4.name == "S_4"
    assert Sym_4.Id == list(range(4))
    assert Sym_4.inverse(Sym_4.Id) == Sym_4.Id
    assert Sym_4.inverse([3, 1, 0, 2]) == [2, 1, 3, 0]
    assert Sym_4.operation([3, 2, 1, 0], [0, 3, 2, 1]) == [3, 0, 1, 2]

    Sym_10 = generate_sym_group(10)
    a = [0, 5, 9, 1, 8, 2, 6, 4, 7, 3]
    b = [0, 3, 5, 9, 7, 1, 6, 8, 4, 2]
    assert Sym_10.inverse(a) == b
    assert Sym_10.operation(a, b) == Sym_10.Id
    assert Sym_10.operation(a, a, True, False) == Sym_10.Id
    assert Sym_10.operation(a, b, True, False) == Sym_10.operation(b, b)
    assert Sym_10.operation(a, Sym_10.Id, False, False) == a
    assert Sym_10.operation(a, Sym_10.Id, True, False) == b
    assert Sym_10.operation(a, Sym_10.Id, False, True) == a
    assert Sym_10.operation(Sym_10.Id, a) == a

    c = [0, 2, 3, 4, 5, 8, 7, 6, 9, 1]

    # Test canonization
    print("Testing canonization")
    assert Sym_10.canonize(Word([a, b], [False, False])) == Sym_10.Id

    word = Word([c, a, b], [True, False, False])
    assert Sym_10.inverse(c) == Sym_10.canonize(word)
    word = Word([c, a, b], [False, False, False])
    assert c == Sym_10.canonize(word)
    word = Word([c, a, b], [True, True, True])
    assert Sym_10.inverse(c) == Sym_10.canonize(word)
    word = Word([a, b, c], [True, True, False])
    assert c == Sym_10.canonize(word)
    word = Word([a, b, c, c, b, b, a], [True, True, False, True, False, False, False])
    assert b == Sym_10.canonize(word)

    # Test concatenation, inversion of words
    assert (
        Word([a, b, c, c], [True, True, False, True])
        * Word([b, b, a], [False, False, False])
    ) == word

    assert (~word).indices == [False, False, True, False, True, True, True]
    assert Sym_10.inverse(Sym_10.canonize(word)) == Sym_10.canonize(~word)

    print("All unit tests passed!")
