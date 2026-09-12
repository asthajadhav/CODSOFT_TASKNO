# Movie Recommendation System

movies = {
    "action": [
        "Avengers",
        "John Wick",
        "Mission Impossible"
    ],
    "comedy": [
        "3 Idiots",
        "Hera Pheri",
        "Dhamaal"
    ],
    "romance": [
        "Jab We Met",
        "Yeh Jawaani Hai Deewani",
        "Dilwale Dulhania Le Jayenge"
    ],
    "horror": [
        "The Conjuring",
        "Insidious",
        "Annabelle"
    ],
    "sci-fi": [
        "Interstellar",
        "The Martian",
        "Inception"
    ]
}

print("==============================")
print("   MOVIE RECOMMENDATION SYSTEM")
print("==============================")

print("\nAvailable genres:")
print("1. Action")
print("2. Comedy")
print("3. Romance")
print("4. Horror")
print("5. Sci-Fi")

choice = input("\nEnter your favourite genre: ").lower().strip()

if choice in movies:
    print("\nRecommended movies for you:")

    for movie in movies[choice]:
        print("⭐", movie)

else:
    print("\nSorry! This genre is not available.")
    print("Please choose from the available genres.")

print("\nThank you for using the Movie Recommendation System!")