try:
    with open("nonexistent_file.txt", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("The specified file does not exist.")
