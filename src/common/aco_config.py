"""Configuration class for the Ant Colony Optimization algorithm."""

from dataclasses import dataclass


@dataclass
class ACOConfig:
    """
    Configuration for the Ant Colony Optimization (ACO) algorithm.

    Attributes
    ----------
    max_weight : int
        Maximum weight of the knapsack.
    alpha : float
        Influence of pheromone on decision-making. Higher means more influence.
    beta : float
        Influence of heuristic information on decision-making. Higher means more influence.
    evaporation_rate : float
        Rate of pheromone evaporation. Higher means faster evaporation.
    q : float
        Constant for pheromone update based on solution quality.
    n_ants : int
        Number of ants in the optimization process. More ants may improve exploration.
    n_iterations : int
        Number of iterations for the algorithm. More iterations allow better convergence.

    Methods
    -------
    __init__(self, alpha, beta, evaporation_rate, Q, n_ants, n_iterations):
        Initializes ACO configuration with provided parameters.
    """

    max_weight: int = 100
    alpha: float = 1.0
    beta: float = 2.0
    evaporation_rate: float = 0.5
    q: float = 100.0
    n_ants: int = 10
    n_iterations: int = 300
