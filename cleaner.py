import os
import shutil # used to move files
from datetime import datetime #This imports the datetime library for timestamps

#This finds your 'user' folder automatically.
home = os.path.expanduser("~")
folder_path = os.path.join(home, "Downloads")
#this will create a folder inside downloads to keep it neat.
target_folder = os.path.join(folder_path, "PowerPoint_Backups")
log_file = os.path.join(folder_path, "activity_log.txt") # the new log file.

print(f"Now Scanning: {folder_path} for files.")

#create backup folder if it doesnt exist yet.
if not os.path.exists(target_folder):
    os.makedirs(target_folder)
    print(f"Created: {target_folder}")

files = os.listdir(folder_path)

#'a' appends at the end of the file instead of overwriting it.
with open(log_file, "a", encoding="utf-8") as log: #utf-8 handles special characters
    for file_name in files:
        #look for .ppt or .pptx
        if file_name.lower().endswith((".ppt", ".pptx")):
            #get the current time for the log.
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            old_path = os.path.join(folder_path, file_name)
            new_path = os.path.join(target_folder, file_name)
            
            #write to the file and the terminal
            log_entry = f"[{timestamp}] MOVED: {file_name}\n"
            log.write(log_entry)
            print(log_entry.strip())