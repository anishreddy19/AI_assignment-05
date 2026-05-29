# AI_assignment-05
# AI Assignment 5

**Name:** B. Sai Anish Reddy  
**Roll No:** SE24UCSE083

---

# Introduction

This repository contains implementations of several important Artificial Intelligence concepts and techniques. The assignment is divided into four major components:

- Game Tree Search Algorithms
- AI-Based Travel Recommendation System
- Knowledge Graph Construction and Querying
- Bayesian Network Inference

Each module demonstrates a different aspect of AI, ranging from decision-making and search to knowledge representation and probabilistic reasoning.

---

# Repository Structure

```text
AI_Assignment_5/
│
├── search_algorithms/
│   ├── tic_tac_toe.py
│   ├── minimax.py
│   ├── alphabeta.py
│   ├── heuristic_alphabeta.py
│   ├── mcts.py
│   └── tests.py
│
├── travel_planner.py
├── knowledgebase.py
├── bayesian_networks.py
└── README.md
```

---

# Part 1: Search Algorithms

The `search_algorithms` directory contains implementations of four search techniques. All algorithms are evaluated using a Tic-Tac-Toe game environment.

## Tic-Tac-Toe Environment

**File:** `tic_tac_toe.py`

This file serves as the common game engine for all search algorithms. It provides functionalities such as:

- Creating and managing the game board
- Making and undoing moves
- Detecting winning conditions
- Checking draw states
- Generating valid moves

---

## Minimax Search

**File:** `minimax.py`

Minimax is a classical adversarial search algorithm used in two-player games. It explores the complete game tree and assumes that both players make optimal decisions.

### Evaluation Scores

| Result | Score |
|----------|---------|
| X Wins | +1 |
| O Wins | -1 |
| Draw | 0 |

The maximizing player (X) selects the move with the highest score, while the minimizing player (O) chooses the move with the lowest score.

---

## Alpha-Beta Pruning

**File:** `alphabeta.py`

Alpha-Beta Pruning improves the efficiency of Minimax by eliminating branches that cannot influence the final decision.

### Parameters

- **Alpha (α):** Best value currently available to the maximizer.
- **Beta (β):** Best value currently available to the minimizer.

Whenever:

```text
Alpha ≥ Beta
```

the remaining branch is discarded because further exploration is unnecessary.

### Benefits

- Produces the same optimal move as Minimax
- Reduces the number of explored states
- Improves execution speed

---

## Heuristic Alpha-Beta Search

**File:** `heuristic_alphabeta.py`

This approach combines Alpha-Beta pruning with a depth-limited search strategy.

Instead of searching until terminal states, the algorithm stops at a predefined depth and estimates board quality using a heuristic evaluation function.

### Heuristic Considerations

- Two symbols in a row
- One symbol in a row
- Potential winning opportunities
- Blocking opportunities

This makes the algorithm suitable for larger search spaces where exhaustive exploration is impractical.

---

## Monte-Carlo Tree Search (MCTS)

**File:** `mcts.py`

Monte-Carlo Tree Search is a simulation-based search technique that balances exploration and exploitation.

### MCTS Process

1. **Selection**
   - Chooses the most promising node using UCB1.

2. **Expansion**
   - Adds a new node to the search tree.

3. **Simulation**
   - Plays random games from the selected state.

4. **Backpropagation**
   - Updates visit counts and win statistics.

After a fixed number of iterations, the move with the highest visit count is selected.

---

# Testing and Validation

**File:** `tests.py`

Three test scenarios are used to validate the correctness of all search algorithms.

## Test Case 1: Winning Opportunity

X already has two symbols in a row and should choose the winning move.

**Expected Move:** `2`

---

## Test Case 2: Defensive Block

O is one move away from winning. X must block the threat.

**Expected Move:** `2`

---

## Test Case 3: Empty Board

The board is initially empty.

**Expected Move:** `4`

The center position is generally considered the strongest opening move.

---

## Sample Result

```text
TEST CASE 1: Winning Move
Expected Move: 2

Minimax        → Move: 2 | PASS
Alpha-Beta     → Move: 2 | PASS
Heuristic AB   → Move: 2 | PASS
MCTS           → Move: 2 | PASS
```

---

# Part 2: AI Travel Planner

**File:** `travel_planner.py`

This module implements a simple rule-based travel recommendation system that suggests destinations based on user preferences.

## Recommendation Criteria

| Factor | Score |
|----------|---------|
| Budget Match | +3 |
| Travel Style Match | +2 |
| Matching Interest | +1 each |

The destination with the highest score is selected as the recommended travel option.

---

## Supported Destinations

- Goa
- Manali
- Jaipur
- Rishikesh

---

## Features

For the recommended destination, the planner generates:

- Estimated travel budget
- Suggested trip duration
- Day-wise itinerary
- Local food recommendations
- Personalized travel activities

---

## Example

```text
Enter Budget (low / medium / high): medium
Enter Travel Type: beach
Enter Interests: beach, nightlife
```

Output:

```text
Recommended Destination: Goa

Score: 7
Duration: 3 Days
Estimated Cost: ₹8,000

Day 1:
Visit Baga Beach

Day 2:
Enjoy Water Sports

Day 3:
Explore Local Markets and Nightlife
```

---

# Part 3: Knowledge Graph

**File:** `knowledgebase.py`

This component demonstrates knowledge representation using a graph-based approach built with NetworkX.

The knowledge graph models relationships among students, books, authors, and genres in a library environment.

---

## Entities Included

### Student

- Student

### Books

- Harry Potter
- The Hunger Games
- The Maze Runner
- The Chronicles of Narnia

### Authors

- J.K. Rowling
- Suzanne Collins
- James Dashner
- C.S. Lewis

### Genres

- Fantasy
- Dystopian Fiction
- Science Fiction

---

## Relationship Types

### borrowed

Connects students with borrowed books.

### written_by

Connects books with their authors.

### belongs_to

Connects books with their genres.

---

## Queries Supported

The graph is used to answer questions such as:

- Which books has the student borrowed?
- Which books were written by C.S. Lewis?
- Which books belong to the Fantasy genre?

---

## Visualization

The graph is visualized using NetworkX and Matplotlib, allowing users to observe entity relationships graphically.

---

# Part 4: Bayesian Networks

**File:** `bayesian_networks.py`

This module demonstrates probabilistic reasoning using a Bayesian Network implemented with pgmpy.

---

## Network Architecture

```text
Rain ─────► WetGrass ◄───── Sprinkler
 │
 ▼
Traffic
```

The model captures dependencies between weather conditions and their effects.

---

## Variables

### Rain

```text
P(Rain = True) = 0.3
```

### Sprinkler

```text
P(Sprinkler = On) = 0.4
```

### WetGrass

Dependent on:

- Rain
- Sprinkler

### Traffic

Dependent on:

- Rain

---

## Inference Technique

The network uses the Variable Elimination algorithm to perform probabilistic inference.

---

## Example Queries

### Probability of Wet Grass

```text
P(WetGrass)
```

### Probability of Rain Given Wet Grass

```text
P(Rain | WetGrass = Wet)
```

### Probability of Heavy Traffic Given Rain

```text
P(Traffic = Heavy | Rain = True)
```

---

## Sample Output

```text
Network Valid: True

P(WetGrass)
Wet: 0.4026

P(Rain | WetGrass = Wet)
Rain: 0.6584

P(Traffic = Heavy | Rain = True)
Heavy: 0.75
```

---

# Required Libraries

Install the necessary packages using:

```bash
pip install pgmpy networkx matplotlib
```

---

# Execution Instructions

### Run Search Algorithm Tests

```bash
cd search_algorithms
python tests.py
```

### Run Travel Planner

```bash
python travel_planner.py
```

### Run Knowledge Graph Module

```bash
python knowledgebase.py
```

### Run Bayesian Network Module

```bash
python bayesian_networks.py
```

---

# Conclusion

This assignment provides practical implementations of several fundamental AI techniques, including game-tree search, intelligent recommendation systems, knowledge representation through graphs, and probabilistic inference using Bayesian networks. Together, these modules demonstrate how AI methods can be applied to solve decision-making, reasoning, and recommendation problems in different domains.

---

## Author

**B. Sai Anish Reddy**  
**Roll No:** SE24UCSE083  
**Course:** Artificial Intelligence
