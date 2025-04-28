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
