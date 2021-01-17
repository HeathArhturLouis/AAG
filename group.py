from abc import ABC, abstractclassmethod, abstractmethod
from word import Word


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


if __name__ == "__main__":
    pass
