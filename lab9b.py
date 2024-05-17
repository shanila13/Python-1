#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 13:02:55 2024

@author: shanilaparveen
lab 9b 
"""
#using code provided by professor as the base 
import random
import matplotlib.pyplot as plt
import numpy as np

# Define the Agent class
class Agent:
    def __init__(self, agent_type, x, y):
        self.agent_type = agent_type
        self.x = x
        self.y = y

    def is_happy(self, world, threshold):
        same_type_neighbors = 0
        total_neighbors = 0

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                neighbor_x = (self.x + dx) % world.size
                neighbor_y = (self.y + dy) % world.size
                neighbor = world.grid[neighbor_x][neighbor_y]
                if neighbor is not None:
                    total_neighbors += 1
                    if neighbor.agent_type == self.agent_type:
                        same_type_neighbors += 1

        if total_neighbors == 0:
            return True  # No neighbors, so agent is happy
        return (same_type_neighbors / total_neighbors) >= threshold

    def move(self, world):
        empty_spots = [(i, j) for i in range(world.size) for j in range(world.size) if world.grid[i][j] is None]
        new_spot = random.choice(empty_spots)
        world.grid[self.x][self.y] = None
        self.x, self.y = new_spot
        world.grid[self.x][self.y] = self

#defining world classa
class World:
    def __init__(self, size, num_agents, threshold):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]
        self.threshold = threshold
        self.agents = []

        for _ in range(num_agents):
            while True:
                x, y = random.randint(0, size-1), random.randint(0, size-1)
                if self.gri[x][y] is None:
                    agent_type = random.choice(['red', 'blue'])
                    agent = Agent(agent_type, x, y)
                    self.grid[x][y] = agent
                    self.agents.append(agent)
                    break       
     #Check Happiness and Move: 
    def step(self):
        random.shuffle(self.agents)
        for agent in self.agents:
            if not agent.is_happy(self, self.threshold):
                agent.move(self)

    def display(self):
        image = np.zeros((self.size, self.size, 3))
        for x in range(self.size):
            for y in range(self.size):
                agent = self.grid[x][y]
                if agent:
                    if agent.agent_type == 'red':
                        image[x, y] = [1, 0, 0]
                    else:
                        image[x, y] = [0, 0, 1]
        plt.imshow(image)
        plt.show()
        
        
        
# Define the Agent and World classes as above

# Parameters
size = 50
num_agents = 100
threshold = 0.3
steps = 60

# Initialize world
world = World(size, num_agents, threshold)

# Run the simulation
for _ in range(steps):
    world.step()
    world.display()