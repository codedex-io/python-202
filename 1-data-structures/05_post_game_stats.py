# Post Game Stats 🏈
# Codédex

# Task 1: Create Player Data
players_data = [
  {"name": "Patrick Mahomes", "position": "Quarterback", "jersey_number": 15, "yards_gained": 400, "touchdowns": 3},
  {"name": "Tyreek Hill", "position": "Wide Receiver", "jersey_number": 10, "yards_gained": 150, "touchdowns": 2},
  # Add more players as needed
]

names = [player["name"] for player in players_data]
print("Players Names:", names)

# Task 2: Analyze Player Positions
positions = [player["position"] for player in players_data]
print("Player Positions:", positions)

# Task 3: Update Player Statistics
players_data[0]["yards_gained"] += 50
players_data[0]["touchdowns"] += 1

# Task 4: Calculate Average Stats
average_yards = sum(player["yards_gained"] for player in players_data) / len(players_data)
average_touchdowns = sum(player["touchdowns"] for player in players_data) / len(players_data)
print("Average Yards Gained:", average_yards)
print("Average Touchdowns:", average_touchdowns)
