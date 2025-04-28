import numpy as np          
import matplotlib.pyplot as plt
import random
from math import sqrt

# Params of the genetic algorithm
GENERATIONS = 1000
POPULATION_SIZE = 200
MUTATION_RATE = 0.05

# All the points we will work with
locations = dict( 
    Arad=(91, 492), Bucharest=(400, 327), Craiova=(253, 288), 
    Drobeta=(165, 299), Eforie=(562, 293), Fagaras=(305, 449), 
    Giurgiu=(375, 270), Hirsova=(534, 350), Iasi=(473, 506), 
    Lugoj=(165, 379), Mehadia=(168, 339), Neamt=(406, 537), 
    Oradea=(131, 571), Pitesti=(320, 368), Rimnicu=(233, 410), 
    Sibiu=(207, 457), Timisoara=(94, 410), Urziceni=(456, 350), 
    Vaslui=(509, 444), Zerind=(108, 531))

# Calculate the distance between 2 cities
def calculate_distance(city1, city2):
    x1, y1 = locations[city1]
    x2, y2 = locations[city2]

    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Creating a table of the distances between every city
CITY_NAMES = list(locations.keys())
ROUTE_SIZE = len(CITY_NAMES)
DIST_MATRIX = np.zeros((ROUTE_SIZE, ROUTE_SIZE))

for i in range(ROUTE_SIZE):
    for j in range(i + 1, ROUTE_SIZE):
        city1 = CITY_NAMES[i]
        city2 = CITY_NAMES[j]
        dist = calculate_distance(city1, city2)
        DIST_MATRIX[i, j] = dist
        DIST_MATRIX[j, i] = dist

# Calculating the distance of a route
def route_distance(route):
    distance = 0
    for i in range(ROUTE_SIZE - 1):
        distance += DIST_MATRIX[route[i], route[i + 1]]
    distance += DIST_MATRIX[route[ROUTE_SIZE - 1], route[0]]

    return distance

# Create a randomly generated route
def create_individual():
    return random.sample(range(ROUTE_SIZE), ROUTE_SIZE)

# Create the initial population
def initialize_population():
    population = []
    for _ in range(POPULATION_SIZE):
        individual = create_individual()
        population.append(individual)

    return population

# Selecting the best POPULATION_SIZE individuals from the population (SELECTION)
def select_best(population):
    sorted_population = sorted(population, key = lambda x: route_distance(x))
    
    return sorted_population[:POPULATION_SIZE]

# Creating new individuals based on the current population (Order Crossover Operator)
def ordered_crossover(parent1, parent2):
    child1 = [None] * ROUTE_SIZE
    child2 = [None] * ROUTE_SIZE
    
    # Chosing 2 point for the crossover
    a, b = sorted(random.sample(range(ROUTE_SIZE), 2))
    
    # Giving the children the segment of the first parent
    child1[a:b] = parent1[a:b]
    child2[a:b] = parent2[a:b]
    
    # Getting the remaining segments
    remaining1 = list(filter(lambda gene: gene not in child1[a:b], parent2))
    remaining2 = list(filter(lambda gene: gene not in child2[a:b], parent1))
    
    # Giving the the children the rest of the segments from the parents
    child1[:a] = remaining1[:a]
    child1[b:] = remaining1[a:]

    child2[:a] = remaining2[:a]
    child2[b:] = remaining2[a:]

    return child1, child2

# Creating new individuals based on the current population () 

# Mutating the individual by a given rate
def mutation(individual):
    if random.random() < MUTATION_RATE:
        a, b = random.sample(range(ROUTE_SIZE), 2)
        individual[a], individual[b] = individual[b], individual[a]

    return individual

# Evolving the population by SELECTION, CROSSOVER and MUTATION
def evolve_population(population):
    child_population = []

    while len(child_population) < POPULATION_SIZE:
        parent1 = random.choice(population)
        parent2 = random.choice(population)
        
        child1, child2 = ordered_crossover(parent1, parent2)
        
        child1 = mutation(child1)
        child2 = mutation(child2)
        
        child_population.append(child1)
        child_population.append(child2)
    
    best_individuals = select_best(population + child_population)
    
    return best_individuals

# The genetic algorithm
def genetic_algorithm():
    population = initialize_population()
    
    best_individual = None
    best_distance = float('inf')
    
    for generation in range(GENERATIONS):
        population = evolve_population(population)
    
        current_best = population[0]
        current_distance = route_distance(current_best)

        if generation % 100 == 0 or generation == GENERATIONS - 1:
            print(f"Generation {generation}: Best distance = {current_distance:.2f}")
        
        if current_distance < best_distance:
            best_distance = current_distance
            best_individual = current_best
    
    print(f"Best distance found: {best_distance:.2f}")
    print(f"Best route: {best_individual}")
    
    return best_individual, best_distance

# Plot the solution
def plot_route(route):
    plt.figure(figsize=(10, 6))

    x = [locations[CITY_NAMES[i]][0] for i in route]
    y = [locations[CITY_NAMES[i]][1] for i in route]

    x.append(x[0])
    y.append(y[0])

    plt.plot(x, y, 'o-')

    for i, city in enumerate(CITY_NAMES):
        plt.text(locations[city][0], locations[city][1], city)

    plt.title(f"Total Distance: {route_distance(route):.2f}")
    plt.show()

best_route, best_distance = genetic_algorithm()
plot_route(best_route)