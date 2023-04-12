import os

# Set the directory path where the images are located
directory_path = 'rename'

# List all the files in the directory
files = os.listdir(directory_path)

# Filter only .jpg files
jpg_files = [f for f in files if f.lower().endswith('.jpg')]

# Sort the files in alphanumeric order (natural order)
jpg_files.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

# Rename the files sequentially
for i, file in enumerate(jpg_files, start=1):
    # Create the new file name
    new_file_name = f"{i}.jpg"
    
    # Get the full file paths for both old and new file names
    old_file_path = os.path.join(directory_path, file)
    new_file_path = os.path.join(directory_path, new_file_name)
    
    # Rename the file
    os.rename(old_file_path, new_file_path)

print(f"Renamed {len(jpg_files)} files successfully.")
