"""Main module for the Ant Colony Optimization algorithm."""

import pandas as pd
from common import ACOConfig, Item
from heuristic import ACO


def load_items_from_csv(csv_path):
    """
    Load item data from a CSV file.

    Parameters
    ----------
    csv_path : str
        Path to the CSV file containing the item data.

    Returns
    -------
    list of Item
        A list of Item objects loaded from the CSV file.
    """
    df = pd.read_csv(csv_path)
    items = [Item(row["name"], row["weight"], row["value"]) for _, row in df.iterrows()]
    return items


def main():
    """
    Main function to execute the Ant Colony Optimization algorithm for the knapsack problem.

    This function loads item data from a CSV file, initializes the ACO algorithm with the specified
    parameters, runs the optimization, and prints the best solution.
    """

    file_path = "data/server.csv"
    items = load_items_from_csv(file_path)

    aco = ACO(items, ACOConfig())
    solution, _ = aco.run()

    print("\nBest solution found:")
    aco.print_solution(0, solution)


if __name__ == "__main__":
    main()
