# Grammys 🏆
# Codédex

from functools import reduce

playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.8), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]

def longer_than_five_minutes(song):
  return song[1] > 5.00

def minutes_to_seconds(song):
  duration = song[1]
  minutes = duration
  seconds = (duration - minutes) * 100

  return int(minutes * 60 + round(seconds))

def add_durations(total, song):
  duration = song[1]
  return total + duration

filtered_songs = list(filter(longer_than_five_minutes, playlist))

convert_to_seconds = list(map(minutes_to_seconds, playlist))

total_playtime = reduce(add_durations, playlist, 0)

print(filtered_songs) 
print(convert_to_seconds)
print(total_playtime)
