import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do Algoritmo Genético
POPULATION_SIZE = 100
MUTATION_RATE = 0.1
GENERATIONS = 1000

# Solicita ao usuário o número de nós do grafo
num_nodes = int(input("Digite o número de nós do grafo: "))
G = nx.erdos_renyi_graph(n=num_nodes, p=0.4, seed=42)  # Grafo aleatório


# Inicializa uma população de soluções aleatórias
def initialize_population(size, graph):
    return [np.random.randint(0, len(graph.nodes), len(graph.nodes)) for _ in range(size)]


# Função de fitness: conta o número de conflitos
def fitness(individual, graph):
    conflicts = sum(1 for edge in graph.edges if individual[edge[0]] == individual[edge[1]])
    return -conflicts  # Quanto menos conflitos, melhor


# Seleção via torneio
def selection(population, graph):
    tournament = random.sample(population, 5)
    return max(tournament, key=lambda ind: fitness(ind, graph))


# Crossover de um ponto
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child1 = np.concatenate((parent1[:point], parent2[point:]))
    child2 = np.concatenate((parent2[:point], parent1[point:]))
    return child1, child2


# Mutação: altera uma cor aleatória
def mutate(individual, num_colors):
    if random.random() < MUTATION_RATE:
        individual[random.randint(0, len(individual) - 1)] = random.randint(0, num_colors - 1)
    return individual


# Algoritmo Genético Principal
def genetic_algorithm(graph):
    population = initialize_population(POPULATION_SIZE, graph)
    num_colors = len(graph.nodes)

    for generation in range(GENERATIONS):
        population = sorted(population, key=lambda ind: fitness(ind, graph), reverse=True)
        new_population = population[:10]  # Elitismo

        while len(new_population) < POPULATION_SIZE:
            parent1 = selection(population, graph)
            parent2 = selection(population, graph)
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutate(child1, num_colors))
            new_population.append(mutate(child2, num_colors))

        population = new_population

        if fitness(population[0], graph) == 0:
            print(f"Solução encontrada na geração {generation}")
            return population[0]

    return population[0]


# Executando o Algoritmo
graph_coloring_solution = genetic_algorithm(G)
print("Solução encontrada:", graph_coloring_solution)


# Exibir o Grafo Colorido
def draw_colored_graph(graph, solution):
    colors = [solution[node] for node in graph.nodes]
    plt.figure(figsize=(8, 6))
    nx.draw(graph, with_labels=True, node_color=colors, cmap=plt.cm.rainbow, edge_color='gray', node_size=500)
    plt.show()



