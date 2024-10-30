# Packing List 📦
# Codédex

import csv

data = [
  ['Item', 'Quantity'],
  ['Mugs', 2],
  ['Hangers', 30],
  ['Shoes', 2]
]

try:
  with open('packing_list.csv', 'r') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
      print(row)
except FileNotFoundError:
  print('Packing list file not found. Creating a new one.')
  with open('packing_list.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)

    csv_writer.writerows(data)
