import os
import shutil # implemented to move files

#This finds your 'user' folder automatically.
home = os.path.expanduser("~")
folder_path = os.path.join(home, "Downloads")

#this will create a folder inside downloads to keep it neat.
target_folder = os.path.join(folder_path, "PowerPoint_Backups")

print(f"Now Scanning: {folder_path} for files.")

#create backup folder if it doesnt exist yet.
if not os.path.exists(target_folder):
    os.makedirs(target_folder)
    print(f"Created: {target_folder}")

files = os.listdir(folder_path)

for file_name in files:
    #look for .ppt or .pptx
    if file_name.lower().endswith((".ppt", ".pptx")):
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(target_folder, file_name)

        #the move action
        shutil.move(old_path, new_path)
        print(f"Moved: {file_name} -> PowerPoint_Backups")