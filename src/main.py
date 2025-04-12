"""Main module for the Ant Colony Optimization algorithm."""

import pandas as pd
from common import Item
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
    items = [Item(row["weight"], row["value"]) for _, row in df.iterrows()]
    return items


def main():
    """
    Main function to execute the Ant Colony Optimization algorithm for the knapsack problem.

    This function loads item data from a CSV file, initializes the ACO algorithm with the specified
    parameters, runs the optimization, and prints the best solution.
    """

    file_path = "teste.csv"
    max_weight = 50
    items = load_items_from_csv(file_path)

    aco = ACO(items, max_weight, n_ants=20, n_iterations=50)
    solution, value = aco.run()

    print("\nBest solution found:")
    for i, selected in enumerate(solution):
        if selected:
            print(f"Item {i+1} - Weight: {items[i].weight}, Value: {items[i].value}")
    print(f"Total value: {value}")


if __name__ == "__main__":
    main()
