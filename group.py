from abc import ABC, abstractclassmethod
from word import Word


class Group(ABC):
    """Black box for computations related to
    presentation of a platform group"""

    # Type of group element, for type checking
    @property
    def element_t(self):
        raise NotImplementedError

    # The following are methods related to the chosen style of canonization

    @abstractclassmethod
    def canonize(cls, word: Word):
        """Put word into some canonical form"""
        ...


if __name__ == "__main__":
    pass
