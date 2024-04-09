# Grammys 🎵
# Codédex

from functools import reduce

# List of songs with their durations (in minutes)
playlist = [
    ('What Was I Made For?', 3.42),
    ('Just Like That', 5.05),
    ('Song 3', 6.8),
    ('Leave The Door Open', 4.02),
    ('I Can\'t Breath', 4.47),
    ('Bad Guy', 3.14)
]

# Function to insert a song into a sorted list based on duration
def sort(sorted_list, song):
    if not sorted_list:
        return [song]
    else:
        for index, item in enumerate(sorted_list):
            if song[1] < item[1]:
                return sorted_list[:index] + [song] + sorted_list[index:]
        return sorted_list + [song]

# Use reduce() to simulate sorting the playlist based on song durations
sorted_playlist = reduce(sort, playlist, [])

# Display the sorted playlist
print('Sorted Playlist (Ascending Order):', sorted_playlist)
