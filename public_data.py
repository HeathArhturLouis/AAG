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
        return (~ x) * y * x

    def gamma_1(self, a: Word, b: Word) -> Word:
        return (~ u) * v

    def gamma_2(self, a: Word, b: Word) -> Word:
        return (~ v) * u


if __name__ == "__main__":
    pass