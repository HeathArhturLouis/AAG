from user import User
from public_data import PublicData


def run_base_protocol(data: PublicData, N=10):
    """Perform group-based AAG and report results"""
    # Create users
    A = User(data.group,
             data.subgroup_A,
             data.subgroup_B,
             data.beta,
             data.gamma_1,
             N)

    B = User(data.group,
             data.subgroup_B,
             data.subgroup_A,
             data.beta,
             data.gamma_1,
             N)

    # Generate private keys
    A.gen_personal_secret()
    B.gen_personal_secret()

    # Transmit messages
    B.receive_elements(A.transmit_elements())
    A.receive_elements(B.transmit_elements())
    
    # Compute Secret information
    A.compute_common_secret()
    B.compute_common_secret()

    # Validate
    a = A.get_common_secret()
    b = B.get_common_secret()

    print(a)
    print(b)
    print(data.group.operation(a, b))


def run_bitwise_protocol(data: PublicData):
    pass


if __name__ == "__main__":
    from symetric_groups import generate_sym_group
    Sym_5 = generate_sym_group(5)

    # Generators for A_5 in S_5
    A_5 = [[1, 2, 3, 4, 0],
           [1, 2, 0, 3, 4]]

    # Generators for S_4 in S_5
    S_4 = [[1, 2, 3, 0, 4],
           [1, 0, 2, 3, 4]]

    Id = [[0, 1, 2, 3, 4]]

    pd = PublicData(Sym_5, S_4, A_5)
    #pd = PublicData(Sym_5, Id, Id)
    #pd = PublicData(Sym_5, ['a1','a2'], ['b1', 'b2'])

    run_base_protocol(pd, 2)