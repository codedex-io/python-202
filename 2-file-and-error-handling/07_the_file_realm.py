# The File Realm 🗂️
# Codédex

# Task 1: The Movie Codex
movie_data = [
    {"name": "Iron Man", "franchise": "MCU", "year_created": 2008},
    {"name": "Spider Man", "franchise": "MCU", "year_created": 2019},
    {"name": "Harry Potter and the Sorcerer Stone", "franchise": "Wizarding World", "year_created": 2001},
    # Add more characters as needed
]

# Task 2: Read and Display
print("Movie Data:")
for movie in movie_data:
    print(movie)

# Task 3: Analyze and Enhance
total_movies = len(movie_data)
print(f"\nTotal Movies: {total_movies}")

franchise_counts = {}
for movie in movie_data:
    franchise = movie["franchise"]
    franchise_counts[franchise] = franchise_counts.get(franchise, 0) + 1

print("Franchise Representation:")
for franchise, count in franchise_counts.items():
    print(f"{franchise}: {count} movies")

# Task 4: Create the Movie File
with open("movie.txt", "w") as file:
    file.write("Welcome to the Movie Hall of Fame!!\n\n")
    file.write("Movies:\n")
    for character in movie_data:
        file.write(f"- {character['name']} from {character['franchise']} ({character['year_created']})\n")
    file.write("\nStatistics:\n")
    for franchise, count in franchise_counts.items():
        file.write(f"- {franchise}: {count} movies\n")

# Bonus Challenge - Movie Sorting
def sort_movies(movies):
    return sorted(movies, key=lambda x: x["name"])

movie_data_sorted = sort_movies(movie_data)

# Update the Movie file with sorted movies
with open("movie.txt", "w") as file_sorted:
    file_sorted.write("Welcome to the Movie Hall of Fame!\n\n")
    file_sorted.write("Movies (Sorted):\n")
    for movie in movie_data_sorted:
        file_sorted.write(f"- {movie['name']} from {movie['franchise']} ({movie['year_created']})\n")
    file_sorted.write("\nStatistics:\n")
    for franchise, count in franchise_counts.items():
        file_sorted.write(f"- {franchise}: {count} movies\n")


