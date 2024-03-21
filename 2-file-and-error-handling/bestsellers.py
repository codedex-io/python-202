import csv

# Open the magical booklist (CSV file)
csv_file_path = 'bestsellers.csv'

# Task 1: Reading the Booklist
def identify_best_selling_book(file_path):
    best_selling_book = None
    max_sales = 0

    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            sales = int(row['sales in millions'])
            if sales > max_sales:
                max_sales = sales
                best_selling_book = row

    return best_selling_book
# Task 2: Creating a Bragging File
def write_bestseller_info(output_file_path, best_selling_book):
    with open(output_file_path, 'w', newline='') as output_file:
        csv_writer = csv.writer(output_file)
        csv_writer.writerow(['Book', 'Author', 'Sales in Millions'])
        csv_writer.writerow([best_selling_book['Book'], best_selling_book['Author'], best_selling_book['sales in millions']])

# Identify the superstar bestseller
best_selling_book_info = identify_best_selling_book(csv_file_path)

# Share the excitement!
if best_selling_book_info:
    print(f"The bestseller is: {best_selling_book_info['Book']} By: {best_selling_book_info['Author']}")
    # Bonus: Write bestseller info to a new CSV file
    output_file_path = 'bestseller_info.csv'
    write_bestseller_info(output_file_path, best_selling_book_info)
    print(f"Bestselling info written to {output_file_path}")
else:
    print("Oh no! No superstars found.")
