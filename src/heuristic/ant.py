"""Represents an Ant in the Ant Colony Optimization algorithm for the knapsack problem."""

import random

from common import ACOConfig, Item


class Ant:
    """Represents an Ant in the Ant Colony Optimization algorithm for the knapsack problem."""

    def __init__(
        self,
        items: list[Item],
        pheromone: list[float],
        config: ACOConfig,
    ):
        """
        Initialize an Ant object for the ACO algorithm.

        Parameters
        ----------
        items : list of Item
            List of items to be optimized.
        pheromone : list of float
            Pheromone levels for each item.
        config : ACOConfig
            Configuration parameters for the ACO algorithm (alpha, beta, etc.).
        """
        self.items = items
        self.pheromone = pheromone
        self.config = config
        self.solution = [0] * len(items)
        self.total_value = 0
        self.total_weight = 0

    def select_items(self):
        """
        Select items to include in the knapsack based on pheromone levels and
        heuristic values, while considering the weight constraint.

        The selection is done by iterating over the items in a random order.
        The probability of selecting an item is calculated using pheromone levels
        and the heuristic (value/weight ratio). If the total weight does not exceed
        the maximum capacity, the item is selected.

        Updates the total weight and total value of the selected items.
        """
        self.solution = [0] * len(self.items)
        self.total_value = 0
        self.total_weight = 0

        indices = list(range(len(self.items)))
        random.shuffle(indices)

        for i in indices:
            if self.total_weight + self.items[i].weight <= self.config.max_weight:
                pheromone_level = self.pheromone[i] ** self.config.alpha
                heuristic = (
                    self.items[i].value / self.items[i].weight
                ) ** self.config.beta
                probability = pheromone_level * heuristic

                if random.random() < probability:
                    self.solution[i] = 1
                    self.total_weight += self.items[i].weight
                    self.total_value += self.items[i].value

    def update_pheromone(self, pheromone: list[float], q: float):
        """
        Update the pheromone levels based on the ant's solution.

        Pheromone is updated on the selected items. The amount of pheromone deposited
        is proportional to the total value of the solution.

        Parameters
        ----------
        pheromone : list of float
            The pheromone levels for each item.
        q : float
            A constant used in the pheromone update formula.
        """
        for i, selected in enumerate(self.solution):
            if selected == 1:
                pheromone[i] += q * self.total_value / (1 + self.total_weight)

    def get_solution(self):
        """
        Get the current solution of the ant.

        Returns
        -------
        list of int
            A list where 1 indicates that the item is selected, and 0 means it's not.
        """
        return self.solution

    def get_total_value(self):
        """
        Get the total value of the selected items.

        Returns
        -------
        int
            The total value of the items selected by the ant.
        """
        return self.total_value

    def get_total_weight(self):
        """
        Get the total weight of the selected items.

        Returns
        -------
        int
            The total weight of the items selected by the ant.
        """
        return self.total_weight
