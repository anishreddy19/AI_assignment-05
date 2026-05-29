import networkx as nx
import matplotlib.pyplot as plt

# Create Knowledge Graph
KG = nx.DiGraph()

# User
KG.add_node("User", type="User")

# Movies
KG.add_node("Inception", type="Movie")
KG.add_node("Interstellar", type="Movie")
KG.add_node("The Dark Knight", type="Movie")
KG.add_node("Avengers: Endgame", type="Movie")

# Directors
KG.add_node("Christopher Nolan", type="Director")
KG.add_node("Anthony Russo", type="Director")

# Genres
KG.add_node("Science Fiction", type="Genre")
KG.add_node("Action", type="Genre")
KG.add_node("Superhero", type="Genre")

# Relationships

# Inception
KG.add_edge(
    "Inception",
    "Christopher Nolan",
    relation="directed_by"
)

KG.add_edge(
    "Inception",
    "Science Fiction",
    relation="belongs_to"
)

# Interstellar
KG.add_edge(
    "Interstellar",
    "Christopher Nolan",
    relation="directed_by"
)

KG.add_edge(
    "Interstellar",
    "Science Fiction",
    relation="belongs_to"
)

# The Dark Knight
KG.add_edge(
    "The Dark Knight",
    "Christopher Nolan",
    relation="directed_by"
)

KG.add_edge(
    "The Dark Knight",
    "Action",
    relation="belongs_to"
)

# Avengers: Endgame
KG.add_edge(
    "Avengers: Endgame",
    "Anthony Russo",
    relation="directed_by"
)

KG.add_edge(
    "Avengers: Endgame",
    "Superhero",
    relation="belongs_to"
)

# User watched movie
KG.add_edge(
    "User",
    "Inception",
    relation="watched"
)

# Display graph information
print("\nMOVIE KNOWLEDGE GRAPH\n")

for source, target, data in KG.edges(data=True):
    print(
        f"{source} --[{data['relation']}]--> {target}"
    )

print("\nMovies watched by User")
for source, target, data in KG.edges(data=True):
    if source == "User" and data["relation"] == "watched":
        print("-", target)

print("\nMovies directed by Christopher Nolan")
for movie, director, data in KG.edges(data=True):
    if director == "Christopher Nolan" and data["relation"] == "directed_by":
        print("-", movie)

print("\nScience Fiction Movies")
for movie, genre, data in KG.edges(data=True):
    if genre == "Science Fiction" and data["relation"] == "belongs_to":
        print("-", movie)

print("\nGraph Statistics")
print("Nodes :", KG.number_of_nodes())
print("Edges :", KG.number_of_edges())

# Visualization
plt.figure(figsize=(14, 10))

pos = nx.spring_layout(
    KG,
    k=2.5,
    iterations=100,
    seed=42
)

nx.draw(
    KG,
    pos,
    with_labels=True,
    node_size=3500,
    font_size=10,
    arrows=True
)

edge_labels = {
    (u, v): d["relation"]
    for u, v, d in KG.edges(data=True)
}

nx.draw_networkx_edge_labels(
    KG,
    pos,
    edge_labels=edge_labels,
    font_size=9
)

plt.title("Movie Recommendation Knowledge Graph")
plt.axis("off")
plt.show()