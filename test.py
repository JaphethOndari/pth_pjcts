def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as f:
            file_content = f.read()
        
        with open(destination_file, 'w') as f:
            f.write(file_content)
        
        print("File copied successfully!")
    
    except FileNotFoundError:
        print("Source file not found.")
# Source file id
source_file = "source.txt"

# Destination file id
destination_file = "destination.txt"

# Copy the contents
copy_file(source_file, destination_file)
