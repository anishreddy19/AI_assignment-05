# AI Assignment 5

**Name:** B.SAI ANISH REDDY
**Roll no:** SE24UCSE083 

---

# Overview

This repository contains implementations of four important Artificial Intelligence concepts:

1. Search Algorithms
2. AI-Based Restaurant Recommendation System
3. Knowledge Graph Construction and Querying
4. Bayesian Network Inference

The project demonstrates decision-making, recommendation systems, knowledge representation, and probabilistic reasoning using Python.

---

# Search Algorithms

All search algorithms are implemented and tested using a Tic-Tac-Toe game environment.

## tic_tac_toe.py

Provides the shared Tic-Tac-Toe game engine used by all search algorithms.

Features:

* Make moves
* Undo moves
* Check winner
* Check draw state
* Generate available moves

---

## minimax.py

Implements the Minimax algorithm.

The algorithm explores the complete game tree and evaluates terminal states:

* X Win → +1
* O Win → -1
* Draw → 0

The maximizing player selects the highest score while the minimizing player selects the lowest score.

---

## alphabeta.py

Implements Alpha-Beta Pruning.

Alpha-Beta improves Minimax by eliminating branches that cannot affect the final outcome.

Features:

* Faster than standard Minimax
* Produces identical optimal moves
* Reduces the number of nodes evaluated

---

## heuristic_ab.py

Implements Heuristic Alpha-Beta Search.

A depth limit is introduced and board positions are evaluated using a heuristic function.

### Heuristic Evaluation

* Two X marks and one empty cell → +10
* Two O marks and one empty cell → -10
* One X mark and two empty cells → +1
* One O mark and two empty cells → -1

This allows faster decision-making in larger search spaces.

---

## mcts.py

Implements Monte Carlo Tree Search (MCTS).

The algorithm performs repeated simulations and selects moves based on statistical outcomes.

### Four Phases

1. Selection
2. Expansion
3. Simulation
4. Backpropagation

The move with the highest visit count is selected as the best move.

---

## Test Cases

The algorithms are tested on several Tic-Tac-Toe board configurations.

### Test 1 – Winning Move

X has an immediate winning move.

### Test 2 – Blocking Move

X must block O from winning.

### Test 3 – Empty Board

Optimal opening move is selected.

### Sample Output

```text
TEST CASE 1: Winning Move
Expected Move: 2

Minimax        → Move: 2 | PASS
Alpha-Beta     → Move: 2 | PASS
Heuristic AB   → Move: 2 | PASS
MCTS           → Move: 2 | PASS
```

---

# AI-Based Restaurant Recommendation System

**File:** `restaurant_recommendation.py`

A rule-based recommendation system that suggests restaurants based on user preferences such as budget, cuisine type, and dining interests.

## Available Restaurants

* Spice Garden
* Ocean Delight
* Pizza Hub
* Dragon Palace

## User Inputs

* Budget (Low / Medium / High)
* Cuisine Type
* Personal Interests

## Cuisine Types

* Indian
* Italian
* Chinese
* Seafood

## Recommendation Scoring

| Criterion              | Score |
| ---------------------- | ----- |
| Budget Match           | +3    |
| Cuisine Type Match     | +2    |
| Each Matching Interest | +1    |

The restaurant with the highest score is selected.

## Generated Recommendation

For the recommended restaurant, the system provides:

* Restaurant Name
* Cuisine Type
* Estimated Cost
* Recommended Dishes

### Example

Input:

```text
Budget: Medium
Cuisine Type: Italian
Interests: Pizza, Friends
```

Output:

```text
Top Recommendation: Pizza Hub

Estimated Cost: ₹700

Must Try Dishes:
- Margherita Pizza
- Pasta Alfredo
- Garlic Bread
```

## Features

* Personalized restaurant recommendations
* Budget-aware suggestions
* Cuisine preference matching
* Interest-based scoring
* Recommended dishes
* Cost estimation

---

# Knowledge Graph

**File:** `knowledge_graph.py`

Builds and visualizes a Movie Recommendation Knowledge Graph using NetworkX.

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

## Supported Queries

* Movies watched by the user
* Movies directed by Christopher Nolan
* Movies belonging to Science Fiction
* Director information for a movie
* Genre information for a movie

## Visualization

The graph is visualized using NetworkX and Matplotlib to show entities and relationships.

---

# Bayesian Network

**File:** `bayesian_network.py`

Implements a Bayesian Network for recommendation inference.

## Variables

* User Preference
* Genre
* Popularity
* Recommendation

## Network Structure

```text
User Preference ──► Recommendation
Genre ───────────► Recommendation
Popularity ──────► Recommendation
```

## Inference Process

1. Collect user preferences.
2. Evaluate available evidence.
3. Compute conditional probabilities.
4. Estimate recommendation likelihood.
5. Generate recommendation outcomes.

## Advantages

* Handles uncertainty
* Supports probabilistic reasoning
* Produces personalized recommendations
* Easily extensible

### Example Query

Given:

* User likes Science Fiction movies
* Popularity is High

Inference:

The Bayesian Network calculates the probability that a movie should be recommended to the user.

---

# Technologies Used

* Python
* NetworkX
* Matplotlib
* NumPy
* pgmpy

---

# Installation

Install required libraries:

```bash
pip install networkx matplotlib pgmpy numpy
```

---

# Project Structure

```text
AI_Assignment_5/
│
├── tic_tac_toe.py
├── minimax.py
├── alphabeta.py
├── heuristic_ab.py
├── mcts.py
├── restaurant_recommendation.py
├── knowledge_graph.py
├── bayesian_network.py
├── README.md
└── .gitignore
```

---

# Learning Outcomes

This assignment demonstrates:

* Adversarial Search
* Minimax Algorithm
* Alpha-Beta Pruning
* Heuristic Search
* Monte Carlo Tree Search
* Recommendation Systems
* Knowledge Representation
* Knowledge Graphs
* Bayesian Networks
* Probabilistic Inference

---

# Conclusion

This project showcases the practical implementation of fundamental Artificial Intelligence techniques. It combines search algorithms, recommendation systems, knowledge graphs, and Bayesian inference to demonstrate how AI can be used for decision-making, information representation, and intelligent recommendations.
