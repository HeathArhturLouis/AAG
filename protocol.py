from user import User
from public_data import PublicData


def run_aag_protocol(data: PublicData, N=10, verbose=False):
    """Perform group-based AAG and report results"""
    # Create users
    if verbose:
        print("--Creating user objects--")

    A = User(data.group, data.subgroup_A, data.subgroup_B, data.beta, data.gamma_1, N)

    B = User(data.group, data.subgroup_B, data.subgroup_A, data.beta, data.gamma_2, N)

    # Generate users' secrets
    A.gen_personal_secret()
    B.gen_personal_secret()

    if verbose:
        print("--Users' Generating Secrets--")
        print()
        print("A's secret | " + str(A._User__secret))
        print("B's secret | " + str(B._User__secret))
        print()

    # Transmit messages
    B.receive_elements(A.transmit_elements())
    A.receive_elements(B.transmit_elements())

    if verbose:
        print("--Transmitting Information--")
        print()
        print("A ---> B:")
        for word in B._User__conj_generators:
            print(word)
        print()
        print("B ---> A:")
        for word in A._User__conj_generators:
            print(word)
        print()

    # Compute Secret information
    A.compute_common_secret()
    B.compute_common_secret()

    if verbose:
        print("--Users Computing Common Secret--")
        print()

    # Validate
    a = A.get_common_secret()
    b = B.get_common_secret()

    # Return users common secrets
    return [a, b]

