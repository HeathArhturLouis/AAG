from types import FunctionType, MethodType
import random
import copy

from group import Group
from word import Word


class User:
    """ Class encapsulating user actions for performing AAG protocol"""

    def __init__(
        self,
        group: Group,
        s_group_own: list,
        s_group_other: list,
        beta: FunctionType,
        gamma: FunctionType,
        N: int = 50,
    ):

        # Public information

        # Group (G)
        self.group: Group = group
        # Subgroups assigned to user
        self.own_group: list = s_group_own
        self.other_group: list = s_group_other
        # Public beta function
        self.beta = beta
        # Gamma function required by user
        self.gamma = gamma

        # Secrete element, received elements
        self.__secret = None
        self.__conj_generators = None
        # conjugate of partner secret, common secret
        self.__conj_secret = None
        self.__common_secret = None

        # Parameters to random element generation algorithm
        self.__N = N

    def gen_personal_secret(self) -> Word:
        """Generate secret element
        (expressed as word in self.s_group)"""
        # Create random product of generators and compose into single word
        self.__secret_g_ind = [
            random.randint(0, len(self.own_group) - 1) for i in range(self.__N)
        ]
        self.__secret = Word(
            [copy.deepcopy(self.own_group[i]) for i in self.__secret_g_ind],
            [False] * len(self.__secret_g_ind),
        )

    def transmit_elements(self) -> list[Word]:
        """Generate and return list of elements for trasmission """
        # Force methods to be run in order
        try:
            assert self.__secret is not None
        except AssertionError:
            raise Exception(
                "Secret key must be generated before \
                            elements can be transmitted"
            )
        # Apply beta with secret to each generator
        return [
            self.beta(self.__secret, Word([gen], [False]))
            for gen in copy.deepcopy(self.other_group)
        ]

    def receive_elements(self, elems: list[Word]):
        """Receive and store elements transmitted by other user and
        compute conjugation of their secret"""
        self.__conj_generators = elems

        list_of_gens = [
            copy.deepcopy(self.__conj_generators[i]) for i in self.__secret_g_ind
        ]

        # Concatenate into conjugate of partner secret
        cs = Word([], [])
        for g in list_of_gens:
            cs = cs * g
        self.__conj_secret = cs

    def compute_common_secret(self, amend: bool = False, amend2=False):
        try:
            assert self.__conj_secret is not None
        except AssertionError:
            raise Exception("Elements must be received from ")
        # Compute word representing common secret
        secret = self.gamma(self.__secret, self.__conj_secret)
        self.__common_secret = self.group.canonise(secret)

    def get_common_secret(self):
        """ Return common secret when computed"""
        try:
            assert self.__common_secret is not None
        except AssertionError:
            raise Exception("Common secret has not been compute yet.")
        return self.__common_secret
