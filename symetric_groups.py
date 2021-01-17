from group import Group, Word


def generate_sym_group(n: int):

    class SymmetricGroup(Group):
        """
        Group operations for Symmetric groups of size n

        Group elements are expected to be lists of length n containing
        the integers from 0 to n-1 corresponding to permutations in two 
        row notation with the index representing the first row and list elements
        the second row.
        """
        size = n
        name = "S_" + str(n)

        # Identity is the empty permutation
        Id = list(range(n))

        @classmethod
        def inverse(cls, a: list[int]) -> list[int]:
            """ Compute the inverse of a permutation by inverting each cycle """
            assert (sorted(a) == cls.Id)
            return [a.index(i) for i in range(cls.size)]

        @classmethod
        def operation(cls, a: list[int], b: list[int], a_ind: bool = False, b_ind: bool = False) -> list[int]:
            """ Compose two permutations
            """
            assert (sorted(a) == cls.Id) and (sorted(b) == cls.Id)
            if(not a_ind):
                a = cls.inverse(a)
            if(not b_ind):
                b = cls.inverse(b) 
            return [a.index(b.index(i)) for i in range(cls.size)]

        @classmethod
        def canonise(cls, word : Word):
            """Put word into canonical form
            in this case the product of its symbols in S_n 
            presented in the two line form"""
            return cls.compute_word(word)

    return SymmetricGroup


if __name__ == "__main__":
    # Unit tests
    # TODO: Move this into pytest

    Sym_3 = generate_sym_group(3)
    assert(Sym_3.size == 3)
    assert(Sym_3.name == "S_3")
    assert(Sym_3.Id == list(range(3)))
    assert(Sym_3.inverse(Sym_3.Id) == Sym_3.Id)
    assert(Sym_3.operation(Sym_3.Id, Sym_3.Id) == Sym_3.Id)
    assert(Sym_3.operation(Sym_3.Id, [2,1,0]) == [2, 1, 0])
    assert(Sym_3.operation([2,1,0], Sym_3.Id) == [2, 1, 0])

    Sym_4 = generate_sym_group(4)
    assert(Sym_4.size == 4)
    assert(Sym_4.name == "S_4")
    assert(Sym_4.Id == list(range(4)))
    assert(Sym_4.inverse(Sym_4.Id) == Sym_4.Id)
    assert(Sym_4.inverse([3, 1, 0, 2]) == [2, 1, 3, 0])
    assert(Sym_4.operation([3, 2, 1, 0], [0, 3, 2, 1]) == [3, 0, 1, 2])

    Sym_10 = generate_sym_group(10)
    a = [0, 5, 9, 1, 8, 2, 6, 4, 7, 3]
    b = [0, 3, 5, 9, 7, 1, 6, 8, 4, 2]
    assert(Sym_10.inverse(a) == b)
    assert(Sym_10.operation(a, b) == Sym_10.Id)
    assert(Sym_10.operation(a, a, True, False) == Sym_10.Id)
    assert(Sym_10.operation(a, b, True, False) == Sym_10.operation(b, b))
    assert(Sym_10.operation(a, Sym_10.Id, False, False) == a)
    assert(Sym_10.operation(a, Sym_10.Id, True, False) == b)
    assert(Sym_10.operation(a, Sym_10.Id, False, True) == a)
    print(Sym_10.operation(Sym_10.Id, a))
    print(a)
    assert(Sym_10.operation(Sym_10.Id, a) == a)

    c = [0, 2, 3, 4, 5, 8, 7, 6, 9, 1]

    # Test cannonisation
    print("Testing Cannonisation")

    print(Sym_10.canonise(Word([a, b],[False, False])))
    
    assert(Sym_10.canonise(Word([a, b],[False, False])) == Sym_10.Id)

    word_1 = Word([c, a, b], [False, False, False])
    print(word_1.indecies)
    assert(Sym_10.inverse(c) == Sym_10.canonise(word_1))
    #assert(Sym_10.canonise(word_1) == c)



    word_2 = Word([a, b, c], [False, True, False])

    d = []
    e = []

    print("All unit tests passed!")
