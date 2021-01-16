from group import Group

def generate_sym_group(n : int):

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
        def inverse(cls, a : list[int]) -> list[int]:
            """ Compute the inverse of a permutation by inverting each cycle """
            assert (sorted(a) == cls.Id)
            return [a.index(i) for i in range(cls.size)]

        @classmethod
        def operation(cls, a: list[int], b: list[int], a_ind: bool = False, b_ind: bool = False) -> list[int]:
            """ Compose two permutations
            """
            assert (sorted(a) == cls.Id) and (sorted(b) == cls.Id)

            if(a_ind):
                a = cls.inverse(a)
            if(b_ind):
                b = cls.inverse(b)

            return [a.index(b.index(i)) for i in range(cls.size)]
    return SymmetricGroup

if __name__ == "__main__":
    # Unit tests
    #TODO: Move this into pytest
       
    Sym_3 = generate_sym_group(3)
    assert(Sym_3.size  == 3)
    assert(Sym_3.name  == "S_3")
    assert(Sym_3.Id == list(range(3)))
    assert(Sym_3.inverse(Sym_3.Id) == Sym_3.Id)
    assert(Sym_3.operation(Sym_3.Id, Sym_3.Id) == Sym_3.Id)

    Sym_4 = generate_sym_group(4)
    assert(Sym_4.size  == 4)
    assert(Sym_4.name  == "S_4")
    assert(Sym_4.Id == list(range(4)))
    assert(Sym_4.inverse(Sym_4.Id) == Sym_4.Id)
    assert(Sym_4.inverse([3,1,0,2]) == [2,1,3,0])
    assert(Sym_4.operation([3,2,1,0],[0,3,2,1]) == [3,0,1,2])

    Sym_10 = generate_sym_group(10)
    a = [0,5,9,1,8,2,6,4,7,3]
    b = [0,3,5,9,7,1,6,8,4,2]
    assert(Sym_10.inverse(a) == b)
    assert(Sym_10.operation(a, b) == Sym_10.Id)

    print("All unit tests passed!")



