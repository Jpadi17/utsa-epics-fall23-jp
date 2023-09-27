import os

folder_path = "C:\\Users\\padil\\OneDrive\\Documents\\python Visual code"  # Replace with the actual folder path
new_prefix = "Jesse"  # The new name prefix

file_list = os.listdir(folder_path)
file_list.sort()  # Sort the file list to maintain the order

counter = 1
for filename in file_list:
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):  # Add more extensions if needed
        extension = os.path.splitext(filename)[1]
        new_name = f"{new_prefix}_{counter:03d}{extension}"
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)
        
        os.rename(old_path, new_path)
        
        counter += 1

print("Renaming complete!")
