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

    def __eq__(self, other):
        """Check equivalence of words (NOT value)"""
        # TODO: Reduction?
        return ((self.elements == other.elements)
                and (self.indecies == other.indecies))

    def reduction(self):
        """Remove reducible pairs from word"""
        # Search for reducible pair
        for i in range(len(self.elements)- 1):
            if ((self.elements[i] == self.elements[i+1])
                    and (self.indecies[i] != self.indecies[i+1])):
                # If reducible pair found, remove and call recursively
                self.elements = self.elements[:i] + self.elements[i+2:]
                self.indecies = self.indecies[:i] + self.indecies[i+2:]
                self.reduction()
                break


if __name__ == "__main__":
    pass
