from symetric_groups import generate_sym_group
from public_data import PublicData

if __name__ == "__main__":
    Sym_5 = generate_sym_group(10)

    # Generators for A_5 in S_5
    A_5 = [[1, 2, 3, 4, 0],
           [1, 2, 0, 3, 4]]

    # Generators for S_4 in S_5
    S_4 = [[1, 2, 3, 0, 4],
           [1, 0, 2, 3, 4]]

    pd = PublicData(group=Sym_5, subgroup_A=S_4, subgroup_B=A_5)

    print(pd)
