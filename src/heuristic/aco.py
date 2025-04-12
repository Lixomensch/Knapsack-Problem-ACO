"""Ant Colony Optimization algorithm for the knapsack problem."""

import numpy as np
from ant import Ant
from common import ACOConfig, Item


class ACO:
    """Ant Colony Optimization algorithm for the knapsack problem."""

    def __init__(self, items: list[Item], max_weight: int, config: ACOConfig):
        """
        Initialize the ACO object.

        Parameters
        ----------
        items : list of Item
            List of items to be optimized.
        max_weight : int
            Maximum weight of the knapsack.
        config : ACOConfig
            Configuration parameters for the ACO algorithm.
        """
        self.items = items
        self.max_weight = max_weight
        self.config = config
        self.pheromone = np.ones(len(items))
        self.best_solution = None
        self.best_value = 0

    def print_solution(self, iteration: int, solution: list[int] = None):
        """
        Display the current best solution and its value.

        Parameters
        ----------
        iteration : int
            Current iteration number.
        solution : list of int, optional
            Current solution indicating selected items.
        """
        print(
            f"Iteration {iteration + 1}/{self.config.n_iterations} | "
            f"Best Value: {self.best_value}"
        )
        if solution:
            for i, selected in enumerate(solution):
                if selected:
                    item = self.items[i]
                    print(f"Item {i+1} - Weight: {item.weight}, Value: {item.value}")

    def run(self):
        """
        Execute the Ant Colony Optimization algorithm.

        Returns
        -------
        best_solution : list of int
            The best binary solution found.
        best_value : int
            The total value of the best solution.
        """
        for iteration in range(self.config.n_iterations):
            ants = [
                Ant(self.items, self.max_weight, self.pheromone, self.config)
                for _ in range(self.config.n_ants)
            ]

            for ant in ants:
                ant.select_items()
                total_value = ant.get_total_value()
                if total_value > self.best_value:
                    self.best_value = total_value
                    self.best_solution = ant.get_solution()

            self.pheromone *= 1 - self.config.evaporation_rate

            for ant in ants:
                ant.update_pheromone(self.pheromone, self.config.q)

            self.print_solution(iteration, self.best_solution)

        return self.best_solution, self.best_value
