import os
import shutil

def move_files(src_folder, dest_folder):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Iterate through all subdirectories and files in the source folder
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            # Get the full path of the file
            file_path = os.path.join(root, file)

            # Move the file to the destination folder
            shutil.move(file_path, os.path.join(dest_folder, file))

if __name__ == "__main__":
    # Specify the source and destination folders
    # Replace these with the actual filepath
    source_directory = "/path/to/source/folder"
    destination_directory = "/path/to/destination/folder"

    # Call the move_files function with the specified directories
    move_files(source_directory, destination_directory)

    print("Files moved successfully.")
