from __future__ import annotations

from abc import ABC, abstractclassmethod, abstractmethod
from dataclasses import dataclass


@dataclass
class Word:
    """
    Word of symbols in a set.each with a 
    corresponding index/power of 1(False) or -1(True) 
    """
    elements: list
    indecies: list[bool]

    def __len__(self):
        assert(len(self.elements) == len(self.indecies))
        return len(self.elements)

    def append(self, elem, index):
        """ Utility method for appending single elements"""
        self.elements.append(elem)
        self.indecies.append(index)

    def __mul__(self, other: Word) -> Word:
        """ Returns concatentaion (*) of two words without changing either."""
        return Word(self.elements + other.elements,
                    self.indecies + other.indecies)

    def __invert__(self):
        """Return word with all elements inverted"""
        return Word(self.elements, [not ind for ind in self.indecies])


class Group(ABC):
    """Black box for computations related to
    presentation of a platform group"""

    # Type of group element
    @property
    def element_t(self):
        raise NotImplementedError
    """
    The following are methods related to the chosen style of canonisation
    for a secure implementation one should acomplish this differently
    """

    # Identity element
    @property
    def Id(self):
        raise NotImplementedError

    @abstractclassmethod
    def operation(cls, a, b, ind_a=False, ind_b=False):
        """Return product of two group elements under group operation.
        Each optionally inverted if index equals True"""
        ...

    @abstractclassmethod
    def inverse(cls, a):
        """ Return the inverse of a."""
        ...

    @classmethod
    def compute_word(cls, word: Word):
        """Compute canonical form of word (array-like) elements by applying the group operation in sequence"""
        if (len(word) == 0):
            # Empty word equals the identity by convention
            return cls.Id
        elif (len(word) == 1):
            if word.indecies[0]:
                return cls.inverse(word.elements[0])
            else:
                return word.elements[0]
        else:
            norm_form = cls.Id
            for i in range(len(word)):
                norm_form = cls.operation(norm_form,
                                          word.elements[i],
                                          b_ind=word.indecies[i])
        return norm_form

    @abstractclassmethod
    def canonise(cls, word: Word):
        """Put word into some canonical form"""
        ...


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
