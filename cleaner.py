import os

#This finds your 'user' folder automatically.
home = os.path.expanduser("~")
folder_path = os.path.join(home, "Downloads")

print(f"Now Scanning: {folder_path} for files.")
files = os.listdir(folder_path)

for file_name in files:
    if file_name.endswith(".ppt"):
        print(f"Found a ppt file: {file_name}")