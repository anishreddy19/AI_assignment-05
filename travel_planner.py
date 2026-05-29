restaurants = [
    {
        "name": "Spice Garden",
        "budget": "low",
        "type": "indian",
        "cost": 300,
        "interests": ["spicy", "vegetarian", "family"],
        "specialties": [
            "Paneer Butter Masala",
            "Dal Tadka",
            "Naan"
        ]
    },

    {
        "name": "Ocean Delight",
        "budget": "high",
        "type": "seafood",
        "cost": 1200,
        "interests": ["seafood", "fine dining", "romantic"],
        "specialties": [
            "Grilled Fish",
            "Prawn Curry",
            "Lobster"
        ]
    },

    {
        "name": "Pizza Hub",
        "budget": "medium",
        "type": "italian",
        "cost": 700,
        "interests": ["pizza", "fast food", "friends"],
        "specialties": [
            "Margherita Pizza",
            "Pasta Alfredo",
            "Garlic Bread"
        ]
    },

    {
        "name": "Dragon Palace",
        "budget": "medium",
        "type": "chinese",
        "cost": 800,
        "interests": ["noodles", "spicy", "family"],
        "specialties": [
            "Hakka Noodles",
            "Manchurian",
            "Spring Rolls"
        ]
    }
]


def recommend_restaurant(budget, food_type, interests):

    recommendations = []

    for restaurant in restaurants:

        score = 0

        # Budget Match
        if restaurant["budget"] == budget:
            score += 3

        # Food Type Match
        if restaurant["type"] == food_type:
            score += 2

        # Interest Match
        for interest in interests:
            if interest in restaurant["interests"]:
                score += 1

        recommendations.append((score, restaurant))

    recommendations.sort(reverse=True, key=lambda x: x[0])

    return recommendations


print("Restaurant Recommendation System")

budget = input(
    "\nEnter Budget (low / medium / high): "
).lower()

food_type = input(
    "Enter Food Type (indian / italian / chinese / seafood): "
).lower()

print("\nEnter interests separated by commas")
print("Example: spicy,family")

interests = input(
    "Your Interests: "
).lower().split(",")

interests = [interest.strip() for interest in interests]

results = recommend_restaurant(
    budget,
    food_type,
    interests
)

print("\nTop Recommendations")

for i in range(min(3, len(results))):

    score, restaurant = results[i]

    print(f"{i+1}. {restaurant['name']} (Score: {score})")

best_score, best_restaurant = results[0]

print("\nRecommended Restaurant")

print("Name:", best_restaurant["name"])
print("Cuisine:", best_restaurant["type"].title())
print("Estimated Cost: Rs.", best_restaurant["cost"])

print("\nMust Try Dishes")

for dish in best_restaurant["specialties"]:
    print("-", dish)

print("\nEnjoy Your Meal!")