from __future__ import annotations
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


if __name__ == "__main__":
    pass
