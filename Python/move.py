import os
import shutil
from math import ceil

source_folder = "C:\\Users\\padil\\OneDrive\\Documents\\python Visual code"
destination_base = "path/to/destination/folders"  # Base path for destination folders
num_destination_folders = 5  # Number of destination folders

# Create destination folders if they don't exist
for i in range(1, num_destination_folders + 1):
    destination_folder = os.path.join(destination_base, f"Folder_{i}")
    os.makedirs(destination_folder, exist_ok=True)

# Get a list of image files in the source folder
image_files = [filename for filename in os.listdir(source_folder) if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

# Calculate images per folder
images_per_folder = ceil(len(image_files) / num_destination_folders)

# Distribute images to destination folders
counter = 1
for image_filename in image_files:
    source_path = os.path.join(source_folder, image_filename)
    destination_folder = os.path.join(destination_base, f"Folder_{counter}")
    destination_path = os.path.join(destination_folder, image_filename)

    shutil.copy(source_path, destination_path)

    counter = (counter % num_destination_folders) + 1

print("Images distributed to folders!")
