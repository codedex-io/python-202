# Bestsellers 📚
# Codédex

import csv

# Open the magical booklist (CSV file)
csv_file_path = 'Bestseller - Sheet1.csv'

best_selling_book = None
max_sales = 0

# Task 1: Reading the CSV file
with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
  csv_reader = csv.reader(csv_file)
  
  # Skip the header row
  csv_file.readline()
  
  for row in csv_reader:
    # Extract sales from the row (assuming 'sales in millions' is the fifth column)
    current_sales = float(row[4])
    
    if current_sales > max_sales:
      max_sales = current_sales
      best_selling_book = row

# Task 2: Creating a new file for bestseller info
output_file_path = 'bestseller_info.csv'
with open(output_file_path, 'w', newline='') as output_file:
  csv_writer = csv.writer(output_file)
  
  # Write header
  csv_writer.writerow(['Book', 'Author', 'Sales in Millions'])
  
  # Write best-selling book info
  csv_writer.writerow([best_selling_book[0], best_selling_book[1], best_selling_book[4]])

# Bonus: Print confirmation message
print('Bestselling info written to', output_file_path)
