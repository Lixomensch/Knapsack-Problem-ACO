# 🐜 Knapsack Problem with Ant Colony Optimization (ACO)

This project implements a heuristic solution for the **Knapsack Problem** using the **Ant Colony Optimization (ACO)** algorithm, with data input from a CSV file and formatted output displaying the best selected items.

## 🧠 Algorithm: Ant Colony Optimization (ACO)

The algorithm simulates the behavior of ants searching for food, depositing pheromones on the most promising paths.

### Main parameters:

- `n_ants`: number of ants
- `n_iterations`: number of iterations
- `alpha`: influence of pheromone
- `beta`: influence of heuristic (value/weight)
- `evaporation_rate`: pheromone evaporation rate

## 📊 CSV Example (`data/server.csv`)

```csv
name,weight,value
Item 1,3,25
Item 2,2,20
Item 3,4,30
Item 4,1,15
```

## ▶️ How to Run

### Prerequisites

- Python 3.8+
- Virtual environment (optional but recommended)

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/Knapsack-Problem-ACO.git
cd Knapsack-Problem-ACO

# Install the dependencies
pip install -r requirements.txt
```

### Execution

```bash
# Using the Makefile
make run

# Or manually
python src/main.py
```

## 🖥️ Expected Output

Example output:

```
Iteration 20/50 | Best Value: 90
Best Solution:
- Item 2 (value: 20, weight: 2)
- Item 3 (value: 30, weight: 4)
- Item 4 (value: 15, weight: 1)
Total Weight: 7 / Max Weight: 10
```

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
