from symmetric_groups import generate_sym_group
from public_data import PublicData
from protocol import run_aag_protocol

if __name__ == "__main__":
    delim_size = 100
    # Generate G
    Sym_5 = generate_sym_group(5)

    # Select generators for subgroups S_A and S_B

    # Generators for A_5 in S_5
    A_5 = [[1, 2, 3, 4, 0], [1, 2, 0, 3, 4]]

    # Generators for S_4 in S_5
    S_4 = [[1, 2, 3, 0, 4], [1, 0, 2, 3, 4]]

    # Print

    # Initialise object with public data (beta, gamma_1 and gamma_2)
    pd = PublicData(group=Sym_5, subgroup_A=S_4, subgroup_B=A_5)

    print("#" * delim_size)
    print("Running AAG protocol for:")
    print()
    print("Platform group | " + Sym_5.name)
    print("S_A generators | " + str(S_4))
    print("S_B generators | " + str(A_5))
    print()
    print("#" * delim_size)

    # Run protocol and report results
    # Set 100 randomizations for user private key generation
    common_secrets = run_aag_protocol(data=pd, N=1, verbose=True)

    print("#" * delim_size)
    print("User A arrives at common secret: " + str(common_secrets[0]))
    print("User B arrives at common secret: " + str(common_secrets[1]))
    print()
    if common_secrets[0] == common_secrets[1]:
        print("PROTOCOL EXECUTED SUCCESSFULLY!")
    else:
        print("USER'S SECRETS DO NOT MATCH! PROTOCOL FAILED.")
    print("#" * delim_size)
