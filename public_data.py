from word import Word
from group import Group
from dataclasses import dataclass


@dataclass
class PublicData:
    """
    Abstraction to hold public (agreed upon) data needed
    for one iteration of AAG
    """

    group: Group

    # Generators of user subgroups
    subgroup_A: list[Group.element_t]
    subgroup_B: list[Group.element_t]

    def beta(self, x: Word, y: Word) -> Word:
        return (~x) * y * x

    def gamma_1(self, u: Word, v: Word) -> Word:
        return (~u) * v

    def gamma_2(self, u: Word, v: Word) -> Word:
        return (~v) * u


if __name__ == "__main__":
    print("Running unit tests")
    from symetric_groups import generate_sym_group

    Sym_5 = generate_sym_group(5)

    # Generators for A_5 in S_5
    A_5 = [[1, 2, 3, 4, 0], [1, 2, 0, 3, 4]]

    # Generators for S_4 in S_5
    S_4 = [[1, 2, 3, 0, 4], [1, 0, 2, 3, 4]]

    # Generate Z_5 in S_5
    Z_5 = [[1, 2, 3, 4, 0]]

    # Test generating a subgroup
    fin = Sym_5.Id
    so_far = [Sym_5.Id]
    for i in range(5):
        fin = Sym_5.operation(fin, Z_5[0])
        assert fin not in so_far or fin == Sym_5.Id
        so_far.append(fin.copy())
    assert fin == Sym_5.Id

    pd = PublicData(Sym_5, Z_5, A_5)

    a = Word([[4, 0, 1, 2, 3]], [False])
    b = Word([[1, 2, 3, 4, 0]], [False])
    # Test beta

    # Test gamma_1 and gamma_2
    assert Sym_5.operation([4, 0, 1, 2, 3], [1, 2, 3, 4, 0]) == Sym_5.Id

    assert Sym_5.canonise(pd.gamma_1(a, b)) == Sym_5.canonise(
        Word([[1, 2, 3, 4, 0], [1, 2, 3, 4, 0]], [False, False])
    )

    assert Sym_5.canonise(pd.gamma_2(a, b)) == Sym_5.operation(
        [4, 0, 1, 2, 3], [4, 0, 1, 2, 3]
    )

    pd = PublicData(group=Sym_5, subgroup_A=S_4, subgroup_B=A_5)

    print("Unit tests passed!")
