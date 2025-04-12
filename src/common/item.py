"""Item class for the knapsack problem."""

from dataclasses import dataclass


@dataclass
class Item:
    """Item class for the knapsack problem."""

    def __init__(self, name, weight, value):
        """
        Initialize an Item with a given weight and value.

        Parameters
        ----------
        weight : int
            The weight of the item.
        value : int
            The value of the item.
        """
        self.name = name
        self.weight = weight
        self.value = value
