# Traveling Salesman Problem (TSP) Solver using Genetic Algorithm

## Description  
This project implements a Genetic Algorithm (GA) to solve the Traveling Salesman Problem (TSP). The goal is to find the shortest possible route that visits a set of cities exactly once and returns to the origin city. The algorithm evolves a population of routes over generations, combining crossover and mutation to improve solutions.

---

## Algorithm Overview  
The Genetic Algorithm follows these steps:  

1. **Initialization**: Generates an initial population of random routes.  
2. **Crossover**: Combines parent routes to create offspring using Order Crossover.  
3. **Mutation**: Introduces small random changes to routes to maintain diversity.  
4. **Selection**: Selects the best routes from the current and new generations based on total distance traveled.  

### Pseudocode  
```python  
Function genetic_algorithm():  
    Initialize population  
    best_individual = None  
    best_distance = infinite  
    For each generation from 1 to N:  
        Evolve the population:  
            Select the best individuals from the current generation  
            Create the new generation through crossover and mutation  
            Keep the new generation  
        Find the best solution in the new generation  
        If new distance is better then update the best solution  
    Return best_individual and best_distance

```

---

## 📦 Dependencies
Ensure the following Python libraries are installed before running the program:
```bash
pip install numpy matplotlib
```

---

## 📊 Example Results
The algorithm was tested with different parameters, yielding the following results:
| Generations | Population Size | Mutation Probability | Distance Traveled |
|-------------|-----------------|----------------------|-------------------|
| 200         |	50              | 0.01                 | 1910.12           |
| 500	      | 100	            | 0.02                 | 1719.79           |
| 1000        |	200	            | 0.05                 | 1589.84           |

Sample Outputs:

### Generations: 200, Population: 50, Mutation: 0.01
![image](https://github.com/user-attachments/assets/46b27cda-77b0-4fc2-a8b5-6ddf6dd3f148)


### Generations: 500, Population: 100, Mutation: 0.02
![image](https://github.com/user-attachments/assets/639a1cad-e08a-4f92-ad47-4255d1b5c677)


### Generations: 1000, Population: 200, Mutation: 0.05
![image](https://github.com/user-attachments/assets/85196ea9-db8d-4385-9d94-19be2a696dfa)

---

## 🚀 Usage
1. Clone the repository or download the source code:
```bash
git clone https://github.com/your-username/tsp-genetic-algorithm.git  
cd tsp-genetic-algorithm
```
2. Run the TSP solver:
```bash
python TSP.py
```
