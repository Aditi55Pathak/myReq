file_path = "data.txt"

with open(file_path, 'w') as file:
    file.write("Hello, World!")

with open(file_path, 'r') as file:
    file.seek(7)  # Move to the 7th character (zero-indexed)
    data = file.read(5)  # Read the next 5 characters
    print(data)  # Output: World

with open(file_path, "r") as file:
    position_before = file.tell()  # Get the current position (start of the file)
    print("Position before reading:", position_before)

    content = file.read(5)  # Read the first 5 characters
    position_after = file.tell()  # Get the current position after reading
    print("Content read:", content)
    print("Position after reading:", position_after)

