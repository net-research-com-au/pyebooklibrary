import os

def find_files(directory):
    # List to store the paths of all files
    file_list = []

    # Walk through all directories and subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Full file path
            file_path = os.path.join(root, file)
            file_list.append(file_path)
            # print("topLevel--> ", root, dirs, files)
    
    return file_list

# Specify the directory to start searching
# directory_to_search = r'C:\path\to\your\directory'  # Change this to your desired directory
directory_to_search = r'C:\Users\dheep\OneDrive\Documents\docs\songs'  # Change this to your desired directory

# Call the function
files = find_files(directory_to_search)

# Print all the files found
for file in files:
    print(file)
