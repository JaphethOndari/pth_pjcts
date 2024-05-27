def read_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line, end='')

    except FileNotFoundError:
        print("File not found.")

filename = "source.txt"

read_file(filename)
