# AI Assignment 5

# Roll no: SE24UCSE083
# NAME : B.SAI ANISH REDDY

## Introduction

This repository contains implementations of several important Artificial Intelligence concepts and techniques. The assignment is divided into four major components:

* Game Tree Search Algorithms
* AI-Based Travel Recommendation System
* Knowledge Graph Construction and Querying
* Bayesian Network Inference

Each module demonstrates a different aspect of AI, ranging from decision-making and search to knowledge representation and probabilistic reasoning.

---

# 1. Game Tree Search Algorithms

This module implements classical AI search algorithms for decision-making in two-player games such as Tic-Tac-Toe.

## Algorithms Implemented

### Minimax Algorithm

Minimax explores the complete game tree and chooses the move that maximizes the player's chances of winning while assuming the opponent plays optimally.

### Alpha-Beta Pruning

Alpha-Beta Pruning improves Minimax by eliminating branches that cannot affect the final decision, significantly reducing the search space.

### Heuristic Alpha-Beta Search

A depth-limited version of Alpha-Beta search that uses a heuristic evaluation function when the search depth limit is reached.

### Monte Carlo Tree Search (MCTS)

MCTS evaluates moves through repeated random simulations and selects moves based on statistical outcomes.

## Features

* Optimal move selection
* Search tree pruning
* Heuristic evaluation
* Simulation-based decision making

---

# 2. AI-Based Travel Recommendation System

The Travel Recommendation System suggests travel destinations based on user preferences such as budget, travel style, and interests.

## Available Destinations

* Goa
* Manali
* Jaipur
* Rishikesh

## Recommendation Factors

* Budget
* Travel Type
* Personal Interests

## Travel Types

* Beach
* Hill Station
* Historical
* Adventure

## Features

* Personalized destination recommendations
* Destination scoring mechanism
* Travel itinerary generation
* Activity suggestions
* Food recommendations
* Cost estimation

## Example Output

The system recommends destinations ranked by suitability score and generates a personalized travel plan including:

* Destination
* Duration
* Estimated Cost
* Activities
* Local Foods
* Matching Interests

---

# 3. Knowledge Graph Construction and Querying

This module demonstrates knowledge representation using a Movie Recommendation Knowledge Graph.

## Entities

### User

* User

### Movies

* Inception
* Interstellar
* The Dark Knight
* Avengers: Endgame

### Directors

* Christopher Nolan
* Anthony Russo

### Genres

* Science Fiction
* Action
* Superhero

## Relationships

* watched
* directed_by
* belongs_to

## Sample Facts

* User watched Inception
* Inception is directed by Christopher Nolan
* Interstellar belongs to Science Fiction
* The Dark Knight belongs to Action
* Avengers: Endgame is directed by Anthony Russo

## Queries Supported

* Movies watched by a user
* Movies directed by a specific director
* Movies belonging to a particular genre
* Director information for a movie
* Genre information for a movie

## Visualization

The knowledge graph is visualized using NetworkX and Matplotlib, allowing easy exploration of entities and relationships.

---

# 4. Bayesian Network Inference

The Bayesian Network models probabilistic relationships involved in recommendation systems.

## Variables

* User Preference
* Genre
* Popularity
* Recommendation

## Dependencies

* User Preference → Recommendation
* Genre → Recommendation
* Popularity → Recommendation

## Inference Process

1. Collect user preferences.
2. Evaluate relevant evidence.
3. Compute conditional probabilities.
4. Generate recommendation probabilities.
5. Select the most likely recommendations.

## Advantages

* Handles uncertainty effectively
* Supports probabilistic reasoning
* Provides personalized recommendations
* Extensible and scalable

---

# Technologies Used

* Python
* NetworkX
* Matplotlib
* NumPy

---

# Project Structure

```text
AI_Assignment_5/
│
├── minimax.py
├── alphabeta.py
├── heuristic_ab.py
├── mcts.py
├── travel_planner.py
├── knowledge_graph.py
├── bayesian_network.py
├── images/
│   └── movie_knowledge_graph.png
│
└── README.md
```

---

# Learning Outcomes

Through this assignment, the following AI concepts were explored:

* Adversarial Search
* Game Tree Algorithms
* Alpha-Beta Pruning
* Heuristic Search
* Monte Carlo Methods
* Knowledge Representation
* Knowledge Graphs
* Recommendation Systems
* Bayesian Reasoning
* Probabilistic Inference

---

# Conclusion

This project provides hands-on implementation of fundamental Artificial Intelligence techniques. It demonstrates how AI methods can be applied to search problems, recommendation systems, knowledge representation, and probabilistic decision-making, offering a comprehensive understanding of core AI concepts.
