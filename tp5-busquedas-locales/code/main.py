import time
import csv
import random
import numpy as np
import matplotlib.pyplot as plt
from environment import Environment, pairQueensInCheck
from algorithms.hill_climbing import hillClimbing
from algorithms.simulated_annealing import simulatedAnnealing
from algorithms.genetic import geneticAlgorithm

# Function to run each algorithm 30 times and gather data


def run_experiments(algorithms, n_queens_values, runs=30):
    results = []

    for algorithm, params in algorithms:
        for n in n_queens_values:
            solution_times = []
            states_explored = []
            optimal_solutions = 0

            for _ in range(runs):
                # Initialize environment
                env = Environment(n)
                start_time = time.time()

                if algorithm.__name__ == "geneticAlgorithm":
                    final_env = algorithm(
                        popSize=100, envSize=n, maxGenerations=100)
                else:
                    final_env = algorithm(env)

                elapsed_time = time.time() - start_time

                # Record execution time and number of states explored
                solution_times.append(elapsed_time)
                states_explored.append(final_env.states_explored)

                # Check if it's an optimal solution (value == 0)
                if final_env.value == 0:
                    optimal_solutions += 1

            # Calculate statistics
            optimal_percentage = (optimal_solutions / runs) * 100
            avg_time = np.mean(solution_times)
            std_time = np.std(solution_times)
            avg_states = np.mean(states_explored)
            std_states = np.std(states_explored)

            # Store results
            results.append({
                'algorithm': algorithm.__name__,
                'n_queens': n,
                'optimal_percentage': optimal_percentage,
                'avg_time': avg_time,
                'std_time': std_time,
                'avg_states': avg_states,
                'std_states': std_states
            })

    return results

# Save overall summary results to a CSV


# Generate boxplot for execution times or states explored


def plot_boxplot(data, title, ylabel, filename):
    plt.boxplot(data)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.savefig(filename)
    plt.close()


# Main execution
if __name__ == "__main__":
    consolidated_file = 'consolidated_experiment_results.csv'
    algorithms = ['hillClimbing', 'simulatedAnnealing', 'geneticAlgorithm']
    n_queens_values = [4, 8, 10, 12, 15]

    # Read the consolidated data from the CSV
    results = []
    with open(consolidated_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            results.append(row)

    # Generate boxplots from consolidated data
    for algorithm in algorithms:
        for n in n_queens_values:
            # Filter data for the current algorithm and n_queens
            filtered_data = [
                row for row in results if row['algorithm'] == algorithm and int(row['n_queens']) == n
            ]

            if filtered_data:
                # Extract execution times and states explored for plotting
                times = [float(row['avg_time']) for row in filtered_data]
                states = [float(row['avg_states']) for row in filtered_data]

                # Generate boxplots
                plot_boxplot(times, f'Execution Time for {algorithm} ({n} Queens)',
                             'Execution Time (s)', f'{algorithm}_{n}_queens_times.png')
                plot_boxplot(states, f'States Explored for {algorithm} ({n} Queens)',
                             'States Explored', f'{algorithm}_{n}_queens_states.png')
